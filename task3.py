import snap
import random
import sys
from datetime import datetime
from queue import Queue 
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter

inital_adopters_arr = [100]
####Function to check if node is inside cluster
def neighbour(graph,A,B,new_behav):
    neighbour_A = []
    for Id in graph.GetNI(A).GetOutEdges():
        if Id != A and Id != B and not new_behav[Id]:
            neighbour_A.append(Id)
    for Id in graph.GetNI(B).GetOutEdges():
        if Id in neighbour_A:
            return True
    return False
####
def cascade_key_node(Graph, threshold, inital_adopters, file):
  q = Queue(maxsize = 0) # Create infinite queue to store data
  #num_init_adopters = []
  num_nodes = 0
  for i in Graph.Nodes():
    num_nodes += 1
  #get the number of total node with original state False
  total_num_nodes_aff = [False] * num_nodes

  #get the initial adopters
  for ID in inital_adopters:
    total_num_nodes_aff[ID] = True
    node = Graph.GetNI(ID)
    for neighbour_id in node.GetOutEdges():
      if not total_num_nodes_aff[neighbour_id]:#If not True: False = not adopt, if not false = True = adopt
        q.put((neighbour_id,1))#put the not adopt nodes into queue
  
  while q.empty() is False:
    ID, num_items = q.get() #choose one of the nodes each time
    if total_num_nodes_aff[ID]:
      continue
    node = Graph.GetNI(ID)
    total_neigh = 0
    neigh_aff = 0
    for neighbour_id in node.GetOutEdges():
      #if the outdegree node of selected node is exist, add 1 node number
      if neighbour_id == ID: 
        continue
      total_neigh += 1
      if total_num_nodes_aff[neighbour_id]:#if the outdegree node of selected node is adopter, add the number of affected nodes
        neigh_aff += 1

    if neigh_aff/total_neigh >= threshold:#Update the status of nodes
      total_num_nodes_aff[ID] = True
      for neighbour_id in node.GetOutEdges():
        if not total_num_nodes_aff[neighbour_id]:
          q.put((neighbour_id, num_items+1))
  #count the number of infected node with new behaviour
  number_of_aff_nodes = 0
  for aff_nodes in total_num_nodes_aff:
    if aff_nodes: #check if it is true
      number_of_aff_nodes += 1
  
  cascade_value = (number_of_aff_nodes - len(inital_adopters))*100 / (num_nodes - len(inital_adopters))
  
  node_aff = 0
  for num in range(num_nodes):
    if total_num_nodes_aff[num]:#if the status is true
      node_aff+=1
  print("Threshold: "+str(threshold)+"   Cascade Percentage: "+str(cascade_value))
  print(str(node_aff)+" Nodes with new behavior")
  #store the information about the cascade threshold and cascade percentage
  try:
    f.write("Current Threshold: "+str(threshold)+"   Cascade Percentage: "+str(cascade_value)+"\n")
    f.write(str(node_aff)+" Nodes with new behaviour\n")
  except:
    print("Error")
    exit()
  cluster_arr = []
  cluster_id = 0
  for num in range(num_nodes):
    if total_num_nodes_aff[num]:
      continue
    inside_cluster = False
    for node in cluster_arr:
      if num in node:
        inside_cluster = True
        break
    if not inside_cluster:
      cluster_id2 = []
      cluster_threshold = Queue(maxsize = 0)
      cluster_id2.append(num)
      cluster_threshold.put(num)

      while cluster_threshold.empty() is False:
                node_id = cluster_threshold.get()
                for Id in Graph.GetNI(node_id).GetOutEdges():
                    if not total_num_nodes_aff[Id] and Id not in cluster_id2:
                        if neighbour(Graph, node_id, Id, total_num_nodes_aff):
                            #append the node id in same cluster in array
                            cluster_id2.append(Id)
                            cluster_threshold.put(Id)
      p = 1 #cluster density
      #calculate the cluster density
      for cluster_node_id in cluster_id2:
          num_neigh = 0
          neigh_inside_cluster = 0
          for neigh_id in Graph.GetNI(cluster_node_id).GetOutEdges():
          #count every neighbour by matching it with evey node id
              num_neigh+=1
              if neigh_id in cluster_id2:
                  #during the matching if there is any node we defined it as neighbour inside the same node, 
                  #add the neighbour number as same cluster
                  neigh_inside_cluster+=1
          if neigh_inside_cluster/num_neigh < p: #check if the cluster density is within 1 
              p = neigh_inside_cluster/num_neigh 

      if len(cluster_id2) >1:
          print("Cluster "+str(cluster_id)+" contains "+str(len(cluster_id2))+" nodes")
          print("Cluster "+str(cluster_id)+" Density: "+str(p))
          try:
              f.write("Cluster contains "+str(len(cluster_id2))+" nodes\n")
              f.write("Cluster Density(p): "+str(p)+"\n")
          except:
              print("Error")
              exit()
      cluster_arr.append(cluster_id2)
      cluster_id+=1
  #Write the result back to the txt file for reference or analysis
  try:
      f.write("Nodes with new behaviour: \n")
  except:
      print("Error")
      exit()
  for i in range(num_nodes):
      if total_num_nodes_aff[i]:
          try:
              f.write(str(i)+" ")
          except:
              print("Error")
              exit()
  for i in range(len(cluster_arr)):
      try:
          f.write("Cluster "+str(i)+"\n")
          f.write(str(cluster_arr[i])+"\n")
      except:
          print("Error")
          exit()
  return 

####graph information
MG = snap.LoadEdgeList(snap.PUNGraph, "FB_data.txt", 0, 1)
snap.DelSelfEdges(MG)

####Get the Rank of each node and arrange them starting with highest rank
random.seed(datetime.now())
PRankH = snap.TIntFltH()
snap.GetPageRank(MG,PRankH)
PRankH_arr=[]
for rk in PRankH:
    PRankH_arr.append((rk,PRankH[rk]))
PRankH_arr.sort(key=itemgetter(1), reverse=True)
try:
    f=open("task3_result.txt","w+")
except:
    print("Error")
for inital_adopters in inital_adopters_arr:
    #we generate the random key node by selecting them within 100 highest rank node obtained
    rand_key_node=[]
    for i in range(inital_adopters):
        rand = random.randint(0,100)
        while PRankH_arr[rand][0] in rand_key_node:
            rand = random.randint(0,100)
        rand_key_node.append(PRankH_arr[rand][0])
    print("Number of initial adopters: "+str(inital_adopters))
    cascade_key_node(MG,0.3,rand_key_node,f)
