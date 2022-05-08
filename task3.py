{\rtf1\ansi\ansicpg950\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red255\green255\blue254;\red0\green0\blue0;
\red19\green120\blue72;\red15\green112\blue1;\red0\green0\blue255;\red101\green76\blue29;\red0\green0\blue109;
\red144\green1\blue18;\red32\green108\blue135;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c3529\c53333\c35294;\cssrgb\c0\c50196\c0;\cssrgb\c0\c0\c100000;\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;
\cssrgb\c63922\c8235\c8235;\cssrgb\c14902\c49804\c60000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl380\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  snap\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  random\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  sys\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  datetime \cf2 \strokec2 import\cf4 \strokec4  datetime\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  queue \cf2 \strokec2 import\cf4 \strokec4  Queue \cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  matplotlib.pyplot \cf2 \strokec2 as\cf4 \strokec4  plt\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  operator \cf2 \strokec2 import\cf4 \strokec4  itemgetter, attrgetter\cb1 \
\
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3 inital_adopters_arr = [\cf5 \strokec5 100\cf4 \strokec4 ]\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf6 \cb3 \strokec6 ####Function to check if node is inside cluster\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl380\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf8 \strokec8 neighbour\cf4 \strokec4 (\cf9 \strokec9 graph\cf4 \strokec4 ,\cf9 \strokec9 A\cf4 \strokec4 ,\cf9 \strokec9 B\cf4 \strokec4 ,\cf9 \strokec9 new_behav\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3     neighbour_A = []\cb1 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  Id \cf7 \strokec7 in\cf4 \strokec4  graph.GetNI(A).GetOutEdges():\cb1 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  Id != A \cf7 \strokec7 and\cf4 \strokec4  Id != B \cf7 \strokec7 and\cf4 \strokec4  \cf7 \strokec7 not\cf4 \strokec4  new_behav[Id]:\cb1 \
\cb3             neighbour_A.append(Id)\cb1 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  Id \cf7 \strokec7 in\cf4 \strokec4  graph.GetNI(B).GetOutEdges():\cb1 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  Id \cf7 \strokec7 in\cf4 \strokec4  neighbour_A:\cb1 \
\cb3             \cf2 \strokec2 return\cf4 \strokec4  \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf7 \strokec7 False\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl380\partightenfactor0
\cf6 \cb3 \strokec6 ####\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl380\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf8 \strokec8 cascade_key_node\cf4 \strokec4 (\cf9 \strokec9 Graph\cf4 \strokec4 , \cf9 \strokec9 threshold\cf4 \strokec4 , \cf9 \strokec9 inital_adopters\cf4 \strokec4 , \cf9 \strokec9 file\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3   q = Queue(maxsize = \cf5 \strokec5 0\cf4 \strokec4 ) \cf6 \strokec6 # Create infinite queue to store data\cf4 \cb1 \strokec4 \
\cb3   \cf6 \strokec6 #num_init_adopters = []\cf4 \cb1 \strokec4 \
\cb3   num_nodes = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  i \cf7 \strokec7 in\cf4 \strokec4  Graph.Nodes():\cb1 \
\cb3     num_nodes += \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3   \cf6 \strokec6 #get the number of total node with original state False\cf4 \cb1 \strokec4 \
\cb3   total_num_nodes_aff = [\cf7 \strokec7 False\cf4 \strokec4 ] * num_nodes\cb1 \
\
\cb3   \cf6 \strokec6 #get the initial adopters\cf4 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  ID \cf7 \strokec7 in\cf4 \strokec4  inital_adopters:\cb1 \
\cb3     total_num_nodes_aff[ID] = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\cb3     node = Graph.GetNI(ID)\cb1 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  neighbour_id \cf7 \strokec7 in\cf4 \strokec4  node.GetOutEdges():\cb1 \
\cb3       \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 not\cf4 \strokec4  total_num_nodes_aff[neighbour_id]:\cf6 \strokec6 #If not True: False = not adopt, if not false = True = adopt\cf4 \cb1 \strokec4 \
\cb3         q.put((neighbour_id,\cf5 \strokec5 1\cf4 \strokec4 ))\cf6 \strokec6 #put the not adopt nodes into queue\cf4 \cb1 \strokec4 \
\cb3   \cb1 \
\cb3   \cf2 \strokec2 while\cf4 \strokec4  q.empty() \cf7 \strokec7 is\cf4 \strokec4  \cf7 \strokec7 False\cf4 \strokec4 :\cb1 \
\cb3     ID, num_items = q.get() \cf6 \strokec6 #choose one of the nodes each time\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  total_num_nodes_aff[ID]:\cb1 \
\cb3       \cf2 \strokec2 continue\cf4 \cb1 \strokec4 \
\cb3     node = Graph.GetNI(ID)\cb1 \
\cb3     total_neigh = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3     neigh_aff = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  neighbour_id \cf7 \strokec7 in\cf4 \strokec4  node.GetOutEdges():\cb1 \
\cb3       \cf6 \strokec6 #if the outdegree node of selected node is exist, add 1 node number\cf4 \cb1 \strokec4 \
\cb3       \cf2 \strokec2 if\cf4 \strokec4  neighbour_id == ID: \cb1 \
\cb3         \cf2 \strokec2 continue\cf4 \cb1 \strokec4 \
\cb3       total_neigh += \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3       \cf2 \strokec2 if\cf4 \strokec4  total_num_nodes_aff[neighbour_id]:\cf6 \strokec6 #if the outdegree node of selected node is adopter, add the number of affected nodes\cf4 \cb1 \strokec4 \
\cb3         neigh_aff += \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 if\cf4 \strokec4  neigh_aff/total_neigh >= threshold:\cf6 \strokec6 #Update the status of nodes\cf4 \cb1 \strokec4 \
\cb3       total_num_nodes_aff[ID] = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\cb3       \cf2 \strokec2 for\cf4 \strokec4  neighbour_id \cf7 \strokec7 in\cf4 \strokec4  node.GetOutEdges():\cb1 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 not\cf4 \strokec4  total_num_nodes_aff[neighbour_id]:\cb1 \
\cb3           q.put((neighbour_id, num_items+\cf5 \strokec5 1\cf4 \strokec4 ))\cb1 \
\cb3   \cf6 \strokec6 #count the number of infected node with new behaviour\cf4 \cb1 \strokec4 \
\cb3   number_of_aff_nodes = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  aff_nodes \cf7 \strokec7 in\cf4 \strokec4  total_num_nodes_aff:\cb1 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  aff_nodes: \cf6 \strokec6 #check if it is true\cf4 \cb1 \strokec4 \
\cb3       number_of_aff_nodes += \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3   \cb1 \
\cb3   cascade_value = (number_of_aff_nodes - \cf8 \strokec8 len\cf4 \strokec4 (inital_adopters))*\cf5 \strokec5 100\cf4 \strokec4  / (num_nodes - \cf8 \strokec8 len\cf4 \strokec4 (inital_adopters))\cb1 \
\cb3   \cb1 \
\cb3   node_aff = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  num \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (num_nodes):\cb1 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  total_num_nodes_aff[num]:\cf6 \strokec6 #if the status is true\cf4 \cb1 \strokec4 \
\cb3       node_aff+=\cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3   \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Threshold: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (threshold)+\cf10 \strokec10 "   Cascade Percentage: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (cascade_value))\cb1 \
\cb3   \cf8 \strokec8 print\cf4 \strokec4 (\cf11 \strokec11 str\cf4 \strokec4 (node_aff)+\cf10 \strokec10 " Nodes with new behavior"\cf4 \strokec4 )\cb1 \
\cb3   \cf6 \strokec6 #store the information about the cascade threshold and cascade percentage\cf4 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 try\cf4 \strokec4 :\cb1 \
\cb3     f.write(\cf10 \strokec10 "Current Threshold: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (threshold)+\cf10 \strokec10 "   Cascade Percentage: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (cascade_value)+\cf10 \strokec10 "\\n"\cf4 \strokec4 )\cb1 \
\cb3     f.write(\cf11 \strokec11 str\cf4 \strokec4 (node_aff)+\cf10 \strokec10 " Nodes with new behaviour\\n"\cf4 \strokec4 )\cb1 \
\cb3   \cf2 \strokec2 except\cf4 \strokec4 :\cb1 \
\cb3     \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Error"\cf4 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 exit\cf4 \strokec4 ()\cb1 \
\cb3   cluster_arr = []\cb1 \
\cb3   cluster_id = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  num \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (num_nodes):\cb1 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  total_num_nodes_aff[num]:\cb1 \
\cb3       \cf2 \strokec2 continue\cf4 \cb1 \strokec4 \
\cb3     inside_cluster = \cf7 \strokec7 False\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  node \cf7 \strokec7 in\cf4 \strokec4  cluster_arr:\cb1 \
\cb3       \cf2 \strokec2 if\cf4 \strokec4  num \cf7 \strokec7 in\cf4 \strokec4  node:\cb1 \
\cb3         inside_cluster = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 break\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 not\cf4 \strokec4  inside_cluster:\cb1 \
\cb3       cluster_id2 = []\cb1 \
\cb3       cluster_threshold = Queue(maxsize = \cf5 \strokec5 0\cf4 \strokec4 )\cb1 \
\cb3       cluster_id2.append(num)\cb1 \
\cb3       cluster_threshold.put(num)\cb1 \
\
\cb3       \cf2 \strokec2 while\cf4 \strokec4  cluster_threshold.empty() \cf7 \strokec7 is\cf4 \strokec4  \cf7 \strokec7 False\cf4 \strokec4 :\cb1 \
\cb3                 node_id = cluster_threshold.get()\cb1 \
\cb3                 \cf2 \strokec2 for\cf4 \strokec4  Id \cf7 \strokec7 in\cf4 \strokec4  Graph.GetNI(node_id).GetOutEdges():\cb1 \
\cb3                     \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 not\cf4 \strokec4  total_num_nodes_aff[Id] \cf7 \strokec7 and\cf4 \strokec4  Id \cf7 \strokec7 not\cf4 \strokec4  \cf7 \strokec7 in\cf4 \strokec4  cluster_id2:\cb1 \
\cb3                         \cf2 \strokec2 if\cf4 \strokec4  neighbour(Graph, node_id, Id, total_num_nodes_aff):\cb1 \
\cb3                             \cf6 \strokec6 #append the node id in same cluster in array\cf4 \cb1 \strokec4 \
\cb3                             cluster_id2.append(Id)\cb1 \
\cb3                             cluster_threshold.put(Id)\cb1 \
\cb3       p = \cf5 \strokec5 1\cf4 \strokec4  \cf6 \strokec6 #cluster density\cf4 \cb1 \strokec4 \
\cb3       \cf6 \strokec6 #calculate the cluster density\cf4 \cb1 \strokec4 \
\cb3       \cf2 \strokec2 for\cf4 \strokec4  cluster_node_id \cf7 \strokec7 in\cf4 \strokec4  cluster_id2:\cb1 \
\cb3           num_neigh = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3           neigh_inside_cluster = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3           \cf2 \strokec2 for\cf4 \strokec4  neigh_id \cf7 \strokec7 in\cf4 \strokec4  Graph.GetNI(cluster_node_id).GetOutEdges():\cb1 \
\cb3           \cf6 \strokec6 #count every neighbour by matching it with evey node id\cf4 \cb1 \strokec4 \
\cb3               num_neigh+=\cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3               \cf2 \strokec2 if\cf4 \strokec4  neigh_id \cf7 \strokec7 in\cf4 \strokec4  cluster_id2:\cb1 \
\cb3                   \cf6 \strokec6 #during the matching if there is any node we defined it as neighbour inside the same node, \cf4 \cb1 \strokec4 \
\cb3                   \cf6 \strokec6 #add the neighbour number as same cluster\cf4 \cb1 \strokec4 \
\cb3                   neigh_inside_cluster+=\cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3           \cf2 \strokec2 if\cf4 \strokec4  neigh_inside_cluster/num_neigh < p: \cf6 \strokec6 #check if the cluster density is within 1 \cf4 \cb1 \strokec4 \
\cb3               p = neigh_inside_cluster/num_neigh \cb1 \
\
\cb3       \cf2 \strokec2 if\cf4 \strokec4  \cf8 \strokec8 len\cf4 \strokec4 (cluster_id2) >\cf5 \strokec5 1\cf4 \strokec4 :\cb1 \
\cb3           \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Cluster "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (cluster_id)+\cf10 \strokec10 " contains "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (\cf8 \strokec8 len\cf4 \strokec4 (cluster_id2))+\cf10 \strokec10 " nodes"\cf4 \strokec4 )\cb1 \
\cb3           \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Cluster "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (cluster_id)+\cf10 \strokec10 " Density: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (p))\cb1 \
\cb3           \cf2 \strokec2 try\cf4 \strokec4 :\cb1 \
\cb3               f.write(\cf10 \strokec10 "Cluster contains "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (\cf8 \strokec8 len\cf4 \strokec4 (cluster_id2))+\cf10 \strokec10 " nodes\\n"\cf4 \strokec4 )\cb1 \
\cb3               f.write(\cf10 \strokec10 "Cluster Density(p): "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (p)+\cf10 \strokec10 "\\n"\cf4 \strokec4 )\cb1 \
\cb3           \cf2 \strokec2 except\cf4 \strokec4 :\cb1 \
\cb3               \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Error"\cf4 \strokec4 )\cb1 \
\cb3               \cf8 \strokec8 exit\cf4 \strokec4 ()\cb1 \
\cb3       cluster_arr.append(cluster_id2)\cb1 \
\cb3       cluster_id+=\cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3   \cf6 \strokec6 #Write the result back to the txt file for reference or analysis\cf4 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 try\cf4 \strokec4 :\cb1 \
\cb3       f.write(\cf10 \strokec10 "Nodes with new behaviour: \\n"\cf4 \strokec4 )\cb1 \
\cb3   \cf2 \strokec2 except\cf4 \strokec4 :\cb1 \
\cb3       \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Error"\cf4 \strokec4 )\cb1 \
\cb3       \cf8 \strokec8 exit\cf4 \strokec4 ()\cb1 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  i \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (num_nodes):\cb1 \
\cb3       \cf2 \strokec2 if\cf4 \strokec4  total_num_nodes_aff[i]:\cb1 \
\cb3           \cf2 \strokec2 try\cf4 \strokec4 :\cb1 \
\cb3               f.write(\cf11 \strokec11 str\cf4 \strokec4 (i)+\cf10 \strokec10 " "\cf4 \strokec4 )\cb1 \
\cb3           \cf2 \strokec2 except\cf4 \strokec4 :\cb1 \
\cb3               \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Error"\cf4 \strokec4 )\cb1 \
\cb3               \cf8 \strokec8 exit\cf4 \strokec4 ()\cb1 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  i \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (\cf8 \strokec8 len\cf4 \strokec4 (cluster_arr)):\cb1 \
\cb3       \cf2 \strokec2 try\cf4 \strokec4 :\cb1 \
\cb3           f.write(\cf10 \strokec10 "Cluster "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (i)+\cf10 \strokec10 "\\n"\cf4 \strokec4 )\cb1 \
\cb3           f.write(\cf11 \strokec11 str\cf4 \strokec4 (cluster_arr[i])+\cf10 \strokec10 "\\n"\cf4 \strokec4 )\cb1 \
\cb3       \cf2 \strokec2 except\cf4 \strokec4 :\cb1 \
\cb3           \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Error"\cf4 \strokec4 )\cb1 \
\cb3           \cf8 \strokec8 exit\cf4 \strokec4 ()\cb1 \
\cb3   \cf2 \strokec2 return\cf4 \strokec4  \cb1 \
\
\pard\pardeftab720\sl380\partightenfactor0
\cf6 \cb3 \strokec6 ####graph information\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3 MG = snap.LoadEdgeList(snap.PUNGraph, \cf10 \strokec10 "FB_data.txt"\cf4 \strokec4 , \cf5 \strokec5 0\cf4 \strokec4 , \cf5 \strokec5 1\cf4 \strokec4 )\cb1 \
\cb3 snap.DelSelfEdges(MG)\cb1 \
\
\pard\pardeftab720\sl380\partightenfactor0
\cf6 \cb3 \strokec6 ####Get the Rank of each node and arrange them starting with highest rank\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3 random.seed(datetime.now())\cb1 \
\cb3 PRankH = snap.TIntFltH()\cb1 \
\cb3 snap.GetPageRank(MG,PRankH)\cb1 \
\cb3 PRankH_arr=[]\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf2 \cb3 \strokec2 for\cf4 \strokec4  rk \cf7 \strokec7 in\cf4 \strokec4  PRankH:\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3     PRankH_arr.append((rk,PRankH[rk]))\cb1 \
\cb3 PRankH_arr.sort(key=itemgetter(\cf5 \strokec5 1\cf4 \strokec4 ), reverse=\cf7 \strokec7 True\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf2 \cb3 \strokec2 try\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3     f=\cf8 \strokec8 open\cf4 \strokec4 (\cf10 \strokec10 "task3_result.txt"\cf4 \strokec4 ,\cf10 \strokec10 "w+"\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf2 \cb3 \strokec2 except\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3     \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Error"\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf2 \cb3 \strokec2 for\cf4 \strokec4  inital_adopters \cf7 \strokec7 in\cf4 \strokec4  inital_adopters_arr:\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3     \cf6 \strokec6 #we generate the random key node by selecting them within 100 highest rank node obtained\cf4 \cb1 \strokec4 \
\cb3     rand_key_node=[]\cb1 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  i \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (inital_adopters):\cb1 \
\cb3         rand = random.randint(\cf5 \strokec5 0\cf4 \strokec4 ,\cf5 \strokec5 100\cf4 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 while\cf4 \strokec4  PRankH_arr[rand][\cf5 \strokec5 0\cf4 \strokec4 ] \cf7 \strokec7 in\cf4 \strokec4  rand_key_node:\cb1 \
\cb3             rand = random.randint(\cf5 \strokec5 0\cf4 \strokec4 ,\cf5 \strokec5 100\cf4 \strokec4 )\cb1 \
\cb3         rand_key_node.append(PRankH_arr[rand][\cf5 \strokec5 0\cf4 \strokec4 ])\cb1 \
\cb3     \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Number of initial adopters: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (inital_adopters))\cb1 \
\cb3     cascade_key_node(MG,\cf5 \strokec5 0.3\cf4 \strokec4 ,rand_key_node,f)\cb1 \
}