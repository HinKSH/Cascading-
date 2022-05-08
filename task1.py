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
\
\cb3 num_of_inital_adopters = [\cf5 \strokec5 1\cf4 \strokec4 , \cf5 \strokec5 10\cf4 \strokec4 , \cf5 \strokec5 20\cf4 \strokec4 , \cf5 \strokec5 40\cf4 \strokec4 , \cf5 \strokec5 100\cf4 \strokec4 ]\cb1 \
\cb3 num_of_test_per_threshold = \cf5 \strokec5 10\cf4 \cb1 \strokec4 \
\cf6 \cb3 \strokec6 ####\cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf8 \strokec8 cascade_percentage\cf4 \strokec4 (\cf9 \strokec9 Graph\cf4 \strokec4 , \cf9 \strokec9 threshold\cf4 \strokec4 , \cf9 \strokec9 num_inital_adopters\cf4 \strokec4 , \cf9 \strokec9 seed\cf4 \strokec4 ):\cb1 \
\cb3   q = Queue(maxsize = \cf5 \strokec5 0\cf4 \strokec4 ) \cf6 \strokec6 # Create infinite queue to store data\cf4 \cb1 \strokec4 \
\cb3   num_init_adopters = []\cb1 \
\cb3   num_nodes = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  i \cf7 \strokec7 in\cf4 \strokec4  Graph.Nodes():\cb1 \
\cb3     num_nodes += \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3   \cf6 \strokec6 #get the number of total node with original state False\cf4 \cb1 \strokec4 \
\cb3   total_num_nodes_aff = [\cf7 \strokec7 False\cf4 \strokec4 ] * num_nodes\cb1 \
\
\cb3   random = snap.TRnd(seed)\cb1 \
\
\cb3   \cf6 \strokec6 #get the initial adopters\cf4 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  i \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (\cf5 \strokec5 0\cf4 \strokec4 , num_inital_adopters):\cb1 \
\cb3     node_id = Graph.GetRndNId(random)\cb1 \
\cb3     num_init_adopters.append(node_id)\cb1 \
\cb3     total_num_nodes_aff[node_id] = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\cb3   \cb1 \
\cb3   \cf2 \strokec2 for\cf4 \strokec4  ID \cf7 \strokec7 in\cf4 \strokec4  num_init_adopters:\cb1 \
\cb3     node = Graph.GetNI(ID)\cb1 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  neighbour_id \cf7 \strokec7 in\cf4 \strokec4  node.GetOutEdges():\cb1 \
\cb3       \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 not\cf4 \strokec4  total_num_nodes_aff[neighbour_id]:\cf6 \strokec6 #If not True: False = not adopt, if not false = True = adopt\cf4 \cb1 \strokec4 \
\cb3         q.put((neighbour_id,\cf5 \strokec5 1\cf4 \strokec4 ))\cf6 \strokec6 #put the not adopt nodes into queue\cf4 \cb1 \strokec4 \
\cb3  \cb1 \
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
\cb3   \cf2 \strokec2 return\cf4 \strokec4  (number_of_aff_nodes - num_inital_adopters)*\cf5 \strokec5 100\cf4 \strokec4  / (num_nodes - num_inital_adopters)\cb1 \
\cf6 \cb3 \strokec6 ####\cf4 \cb1 \strokec4 \
\cb3 MG = snap.LoadEdgeList(snap.PUNGraph, \cf10 \strokec10 "FB_data.txt"\cf4 \strokec4 , \cf5 \strokec5 0\cf4 \strokec4 , \cf5 \strokec5 1\cf4 \strokec4 )\cb1 \
\cb3 snap.DelSelfEdges(MG)\cb1 \
\cb3 snap.SaveEdgeList(MG, \cf10 \strokec10 "test2.txt"\cf4 \strokec4 , \cf10 \strokec10 "Save as tab-separated list of edges"\cf4 \strokec4 )\cb1 \
\cb3 snap.PrintInfo(MG, \cf10 \strokec10 "Status"\cf4 \strokec4 , \cf10 \strokec10 "info2.txt"\cf4 \strokec4 , \cf7 \strokec7 False\cf4 \strokec4 )\cb1 \
\
\cb3 seed_arr = []\cb1 \
\
\cf6 \cb3 \strokec6 #make use of random seed and store it to an array to make thresholds use same sets of init adopters\cf4 \cb1 \strokec4 \
\
\cb3 random.seed(datetime.now())\cb1 \
\cf2 \cb3 \strokec2 for\cf4 \strokec4  i \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (num_of_test_per_threshold):\cb1 \
\cb3     seed_arr.append(\cf11 \strokec11 int\cf4 \strokec4 (\cf5 \strokec5 10000\cf4 \strokec4 *random.random()))\cb1 \
\cb3     \cf6 \strokec6 #print(seed_arr[i])\cf4 \cb1 \strokec4 \
\
\
\cb3 plt.title(\cf10 \strokec10 "Relation between threshold and cascade percentage"\cf4 \strokec4 )\cb1 \
\cb3 plt.xlabel(\cf10 \strokec10 'Threshold'\cf4 \strokec4 )\cb1 \
\cb3 plt.ylabel(\cf10 \strokec10 'Cascade Percentage'\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 ###\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 try\cf4 \strokec4 :\cb1 \
\cb3     f=\cf8 \strokec8 open\cf4 \strokec4 (\cf10 \strokec10 "task1_result.txt"\cf4 \strokec4 ,\cf10 \strokec10 "w+"\cf4 \strokec4 )\cb1 \
\cf2 \cb3 \strokec2 except\cf4 \strokec4 :\cb1 \
\cb3     \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Error"\cf4 \strokec4 )\cb1 \
\
\cf2 \cb3 \strokec2 for\cf4 \strokec4  num \cf7 \strokec7 in\cf4 \strokec4  num_of_inital_adopters:\cb1 \
\cb3     \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Number of initial adopters: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (num))\cb1 \
\cb3     \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Each threshold value has "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (num_of_test_per_threshold)+\cf10 \strokec10 " sets of initial adopters"\cf4 \strokec4 )\cb1 \
\cb3     cascade_percentage_arr = []\cb1 \
\cb3     threshold_value = []\cb1 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  threshold \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 reversed\cf4 \strokec4 (\cf8 \strokec8 range\cf4 \strokec4 (\cf5 \strokec5 99\cf4 \strokec4 )):\cb1 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  threshold > \cf5 \strokec5 15\cf4 \strokec4  \cf7 \strokec7 and\cf4 \strokec4  ((threshold+\cf5 \strokec5 1\cf4 \strokec4 )%\cf5 \strokec5 5\cf4 \strokec4 )!=\cf5 \strokec5 0\cf4 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 continue\cf4 \cb1 \strokec4 \
\cb3         threshold = (threshold+\cf5 \strokec5 1\cf4 \strokec4 )/\cf5 \strokec5 100\cf4 \cb1 \strokec4 \
\cb3         cascade_value = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 for\cf4 \strokec4  rand \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (\cf8 \strokec8 len\cf4 \strokec4 (seed_arr)):\cb1 \
\cb3             cascade_value += cascade_percentage(MG,threshold,num,seed_arr[rand])\cb1 \
\cb3         cascade_value = cascade_value/\cf8 \strokec8 len\cf4 \strokec4 (seed_arr)\cb1 \
\cb3         cascade_percentage_arr.append(cascade_value)\cb1 \
\cb3         threshold_value.append(threshold)\cb1 \
\cb3         \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Threshold: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (threshold)+\cf10 \strokec10 " Cascade Percentage(%): "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (cascade_value))\cb1 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  cascade_value==\cf5 \strokec5 100\cf4 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 break\cf4 \cb1 \strokec4 \
\cb3     plt.plot(threshold_value, cascade_percentage_arr, label = \cf11 \strokec11 str\cf4 \strokec4 (num))\cb1 \
\cb3     \cf2 \strokec2 try\cf4 \strokec4 :\cb1 \
\cb3         f.write(\cf10 \strokec10 "Number of initial adopters: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (num)+\cf10 \strokec10 "\\n"\cf4 \strokec4 )\cb1 \
\cb3         f.write(\cf10 \strokec10 "Each threshold value has "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (num_of_test_per_threshold)+\cf10 \strokec10 " sets of initial adopters\\n"\cf4 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 for\cf4 \strokec4  i \cf7 \strokec7 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (\cf8 \strokec8 len\cf4 \strokec4 (threshold_value)):\cb1 \
\cb3             f.write(\cf10 \strokec10 "Threshold Value: "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (threshold_value[i])+\cf10 \strokec10 " Cascade Percentage(%): "\cf4 \strokec4 +\cf11 \strokec11 str\cf4 \strokec4 (cascade_percentage_arr[i])+\cf10 \strokec10 "\\n"\cf4 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 except\cf4 \strokec4 :\cb1 \
\cb3         \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Error"\cf4 \strokec4 )\cb1 \
\
\cb3 plt.legend(title=\cf10 \strokec10 "Different Number of Initial Adopters"\cf4 \strokec4 )\cb1 \
\cf2 \cb3 \strokec2 try\cf4 \strokec4 :\cb1 \
\cb3     plt.savefig(\cf10 \strokec10 'task1_result.png'\cf4 \strokec4 )\cb1 \
\cf2 \cb3 \strokec2 except\cf4 \strokec4 :\cb1 \
\cb3     \cf8 \strokec8 print\cf4 \strokec4 (\cf10 \strokec10 "Error"\cf4 \strokec4 )\cb1 \
\cb3 plt.show()\cb1 \
}