import snap
import random
import sys
from datetime import datetime
from queue import Queue 
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter

num_of_test_per_threshold = 10
num_of_inital_adopters = [1, 10, 50]

####function for random node effect on cascading behaviour
def cascade_percentage(Graph, threshold, num_inital_adopters, seed):
  q = Queue(maxsize = 0) # Create infinite queue to store data
  num_init_adopters = []
  num_nodes = 0
  for i in Graph.Nodes():
    num_nodes += 1
  #get the number of total node with original state False
  total_num_nodes_aff = [False] * num_nodes

  random = snap.TRnd(seed)

  #get the initial adopters
  for i in range(0, num_inital_adopters):
    node_id = Graph.GetRndNId(random)
    num_init_adopters.append(node_id)
    total_num_nodes_aff[node_id] = True
  
  for ID in num_init_adopters:
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
  
  return (number_of_aff_nodes - num_inital_adopters)*100 / (num_nodes - num_inital_adopters)

####function for key node effect on cascading behaviour
def cascade_key_node(Graph, threshold, inital_adopters):
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
  
  return (number_of_aff_nodes - len(inital_adopters))*100 / (num_nodes - len(inital_adopters))
####graph information
MG = snap.LoadEdgeList(snap.PUNGraph, "FB_data.txt", 0, 1)
snap.DelSelfEdges(MG)
snap.SaveEdgeList(MG, "test2.txt", "Save as tab-separated list of edges")
snap.PrintInfo(MG, "Status", "info2.txt", False)

####graph plotting
plt.title("Relation between threshold and cascade percentage")
plt.xlabel('Threshold')
plt.ylabel('Cascade Percentage')
random.seed(datetime.now())

#get the rank of the nodes
PRankH = snap.TIntFltH()
snap.GetPageRank(MG,PRankH)
PRankH_node=[]

for rk in PRankH:
    PRankH_node.append((rk,PRankH[rk]))
#arrange the node with higher rank to first
PRankH_node.sort(key=itemgetter(1), reverse=True) 

try:
    f=open("task2_result.txt","w+")
except:
    print("Error")

for num in num_of_inital_adopters:
  print("Type of initial adopters: Key Nodes(with high PRank nodes)")
  print("Number of initial adopters: "+str(num))
  print("Each threshold value has "+str(num_of_test_per_threshold)+" sets of initial adopters")
  key_node=[]
  cascade_percentage_arr = []
  threshold_value = []
  for i in range(num_of_test_per_threshold):#loop 10 times
  #we generate the random key node by selecting them within 100 highest rank node obtained
        key_node.append([])
        for j in range(num):
            rand = random.randint(0,100)
            #get the node with high page rank from the pagerank array randomly
            while PRankH_node[rand][0] in key_node[i]:
                rand = random.randint(0,100)
            key_node[i].append(PRankH_node[rand][0])
  
  for threshold in reversed(range(99)):
        if threshold > 15 and ((threshold+1)%5)!=0:
            continue
        threshold = (threshold+1)/100
        cascade_value = 0
        for time in range (num_of_test_per_threshold):
          cascade_value += cascade_key_node(MG,threshold,key_node[time])
        cascade_value = cascade_value/num_of_test_per_threshold
        if cascade_value != 0:
            cascade_percentage_arr.append(cascade_value)
            threshold_value.append(threshold)
            print("Threshold: "+str(threshold)+" Cascade Percentage(%): "+str(cascade_value))
            if cascade_value==100:
                break

  try:
      f.write("Type of initial adopters: Key nodes(with high PRank nodes)\n")
      f.write("Number of initial adopters: "+str(num)+"\n")
      f.write("Each threshold value has "+str(num_of_test_per_threshold)+" sets of initial adopters\n")
      for i in range(len(threshold_value)):
        f.write("Threshold: "+str(threshold_value[i])+" Cascade Percentage(%): "+str(cascade_percentage_arr[i])+"\n")
  except:
        print("Error")
  plt.plot(threshold_value,cascade_percentage_arr,label="Key nodes, Initial Adopters="+str(num))
  

seed_arr = []
for i in range(num_of_test_per_threshold):
    seed_arr.append(int(10000*random.random()))
for num in num_of_inital_adopters:
    print("Number of initial adopters: "+str(num))
    print("Each threshold value has "+str(num_of_test_per_threshold)+" sets of initial adopters")
    cascade_percentage_arr = []
    threshold_value = []
    for threshold in reversed(range(99)):
        if threshold > 20 and ((threshold+1)%5)!=0:
            continue
        threshold = (threshold+1)/100
        cascade_value = 0
        for rand in range(len(seed_arr)):
            cascade_value += cascade_percentage(MG,threshold,num,seed_arr[rand])
        cascade_value = cascade_value/len(seed_arr)
        cascade_percentage_arr.append(cascade_value)
        threshold_value.append(threshold)
        print("Threshold: "+str(threshold)+" Cascade Percentage(%): "+str(cascade_value))
        if cascade_value==100:
            break
    try:
      f.write("Type of initial adopters: Key nodes(with all nodes)\n")
      f.write("Number of initial adopters: "+str(num)+"\n")
      f.write("Each threshold value has "+str(num_of_test_per_threshold)+" sets of initial adopters\n")
      for i in range(len(threshold_value)):
        f.write("Threshold: "+str(threshold_value[i])+" Cascade percentage(%): "+str(cascade_percentage_arr[i])+"\n")
    except:
        print("Error")
    plt.plot(threshold_value,cascade_percentage_arr,label="Random nodes, Initial Adopters="+str(num))
    
plt.legend(title="Number of initial adopters")
try:
    plt.savefig('task2_result.png')
except:
    print("Error")
plt.show()



