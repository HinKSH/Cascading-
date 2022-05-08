{\rtf1\ansi\ansicpg950\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red255\green255\blue254;\red0\green0\blue0;
\red144\green1\blue18;\red19\green120\blue72;\red0\green0\blue255;\red15\green112\blue1;\red101\green76\blue29;
\red32\green108\blue135;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c53333\c35294;\cssrgb\c0\c0\c100000;\cssrgb\c0\c50196\c0;\cssrgb\c47451\c36863\c14902;
\cssrgb\c14902\c49804\c60000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl380\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
import\cf4  snap\cb1 \
\cf2 \cb3 import\cf4  random\cb1 \
\cf2 \cb3 import\cf4  sys\cb1 \
\cf2 \cb3 from\cf4  datetime \cf2 import\cf4  datetime\cb1 \
\cf2 \cb3 from\cf4  queue \cf2 import\cf4  Queue \cb1 \
\cf2 \cb3 import\cf4  matplotlib.pyplot \cf2 as\cf4  plt\cb1 \
\
\cb3 MG = snap.LoadEdgeList(snap.PUNGraph, \cf5 "FB_data.txt"\cf4 , \cf6 0\cf4 , \cf6 1\cf4 )\cb1 \
\cb3 snap.DelSelfEdges(MG)\cb1 \
\cb3 snap.SaveEdgeList(MG, \cf5 "test.txt"\cf4 , \cf5 "Save as tab-separated list of edges"\cf4 )\cb1 \
\cb3 snap.PrintInfo(MG, \cf5 "Status"\cf4 , \cf5 "info.txt"\cf4 , \cf7 False\cf4 )\cb1 \
\
\cb3 edge_arr=[]\cb1 \
\cf2 \cb3 for\cf4  Node \cf7 in\cf4  MG.Nodes():\cf8 #number of Node\cf4 \cb1 \
\cb3     count=\cf6 0\cf4 \cb1 \
\cb3     \cf2 for\cf4  ID \cf7 in\cf4  Node.GetOutEdges():\cf8 #number of edges of each node with particular ID\cf4 \cb1 \
\cb3         count+=\cf6 1\cf4 \cb1 \
\cb3     edge_arr.append(count)\cb1 \
\
\cb3 plt.title(\cf5 "Distribution of Number of Edges"\cf4 )\cb1 \
\cb3 plt.ylabel(\cf5 'Number of edges'\cf4 )\cb1 \
\cb3 plt.xlabel(\cf5 'Node ID'\cf4 )\cb1 \
\cb3 plt.plot(edge_arr)\cb1 \
\
\cf2 \cb3 try\cf4 :\cb1 \
\cb3     plt.savefig(\cf5 'init.png'\cf4 )\cb1 \
\cf2 \cb3 except\cf4 :\cb1 \
\cb3     \cf9 print\cf4 (\cf5 "Error"\cf4 )\cb1 \
\cb3 plt.show()\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf8 \cb3 ##########\cf4 \cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3 edge_arr.sort()\cf8 #rearrange the edges\cf4 \cb1 \
\
\cb3 min_edge = \cf10 str\cf4 (edge_arr[\cf6 0\cf4 ])\cb1 \
\cb3 max_edge = \cf10 str\cf4 (edge_arr[\cf9 len\cf4 (edge_arr)\cf6 -1\cf4 ])\cb1 \
\cb3 ave_edge = \cf10 str\cf4 (\cf9 sum\cf4 (edge_arr)/\cf9 len\cf4 (edge_arr))\cb1 \
\cb3 median = \cf10 str\cf4 (edge_arr[\cf10 int\cf4 (\cf9 len\cf4 (edge_arr)/\cf6 2\cf4 )])\cb1 \
\cb3 num_edge_arr = [\cf6 0\cf4 ] * (\cf10 int\cf4 (max_edge)+\cf6 1\cf4 )\cb1 \
\
\cf2 \cb3 for\cf4  i \cf7 in\cf4  edge_arr:\cb1 \
\cb3     num_edge_arr[i]+=\cf6 1\cf4 \cb1 \
\cb3 plt.title(\cf5 "Relation between the nodes and edges"\cf4 )\cb1 \
\cb3 plt.ylabel(\cf5 'Number of Nodes'\cf4 )\cb1 \
\cb3 plt.xlabel(\cf5 \'91Number of Edges'\cf4 )\cb1 \
\cb3 plt.plot(num_edge_arr)\cb1 \
\
\cf2 \cb3 try\cf4 :\cb1 \
\cb3     plt.savefig(\cf5 'init2.png'\cf4 )\cb1 \
\cf2 \cb3 except\cf4 :\cb1 \
\cb3     \cf9 print\cf4 (\cf5 "Error"\cf4 )\cb1 \
\cb3 plt.show()\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf8 \cb3 ##########\cf4 \cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf9 \cb3 print\cf4 (\cf5 "Minimun number of Edges: "\cf4 +min_edge)\cb1 \
\cf9 \cb3 print\cf4 (\cf5 "Maximun number of Edges: "\cf4 +max_edge)\cb1 \
\cf9 \cb3 print\cf4 (\cf5 "Avergae number of Edges: "\cf4 +ave_edge)\cb1 \
\cf9 \cb3 print\cf4 (\cf5 "Median number of Edges: "\cf4 +median)\cb1 \
\pard\pardeftab720\sl380\partightenfactor0
\cf2 \cb3 try\cf4 :\cb1 \
\cb3     f=\cf9 open\cf4 (\cf5 "init.txt"\cf4 ,\cf5 "w+"\cf4 )\cb1 \
\cb3     f.write(\cf5 "Minimun number of Edges: "\cf4 +min_edge+\cf5 "\\n"\cf4 )\cb1 \
\cb3     f.write(\cf5 "Maximun number of Edges: "\cf4 +max_edge+\cf5 "\\n"\cf4 )\cb1 \
\cb3     f.write(\cf5 "Avergae number of Edges: "\cf4 +ave_edge+\cf5 "\\n"\cf4 )\cb1 \
\cb3     f.write(\cf5 "Median number of Edges: "\cf4 +median+\cf5 "\\n"\cf4 )\cb1 \
\cb3     \cf2 for\cf4  i \cf7 in\cf4  \cf9 range\cf4 (\cf9 len\cf4 (num_edge_arr)):\cb1 \
\cb3         f.write(\cf10 str\cf4 (num_edge_arr[i])+\cf5 " nodes have "\cf4 +\cf10 str\cf4 (i)+\cf5 " edges\\n"\cf4 )\cb1 \
\cf2 \cb3 except\cf4 :\cb1 \
\cb3     \cf9 print\cf4 (\cf5 "Error"\cf4 )\cb1 \
\
\
\
}