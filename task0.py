import snap
import random
import sys
from datetime import datetime
from queue import Queue 
import matplotlib.pyplot as plt

MG = snap.LoadEdgeList(snap.PUNGraph, "FB_data.txt", 0, 1)
snap.DelSelfEdges(MG)
snap.SaveEdgeList(MG, "test.txt", "Save as tab-separated list of edges")
snap.PrintInfo(MG, "Status", "info.txt", False)

edge_arr=[]
for Node in MG.Nodes():#number of Node
    count=0
    for ID in Node.GetOutEdges():#number of edges of each node with particular ID
        count+=1
    edge_arr.append(count)

plt.title("Distribution of Number of Edges")
plt.ylabel('Number of edges')
plt.xlabel('Node ID')
plt.plot(edge_arr)

try:
    plt.savefig('init.png')
except:
    print("Error")
plt.show()
##########
edge_arr.sort()#rearrange the edges

min_edge = str(edge_arr[0])
max_edge = str(edge_arr[len(edge_arr)-1])
ave_edge = str(sum(edge_arr)/len(edge_arr))
median = str(edge_arr[int(len(edge_arr)/2)])
num_edge_arr = [0] * (int(max_edge)+1)

for i in edge_arr:
    num_edge_arr[i]+=1
plt.title("Relation between the nodes and edges")
plt.ylabel('Number of Nodes')
plt.xlabel(‘Number of Edges')
plt.plot(num_edge_arr)

try:
    plt.savefig('init2.png')
except:
    print("Error")
plt.show()
##########
print("Minimun number of Edges: "+min_edge)
print("Maximun number of Edges: "+max_edge)
print("Avergae number of Edges: "+ave_edge)
print("Median number of Edges: "+median)
try:
    f=open("init.txt","w+")
    f.write("Minimun number of Edges: "+min_edge+"\n")
    f.write("Maximun number of Edges: "+max_edge+"\n")
    f.write("Avergae number of Edges: "+ave_edge+"\n")
    f.write("Median number of Edges: "+median+"\n")
    for i in range(len(num_edge_arr)):
        f.write(str(num_edge_arr[i])+" nodes have "+str(i)+" edges\n")
except:
    print("Error")
