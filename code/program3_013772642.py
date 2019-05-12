#!/usr/bin/env python
# coding: utf-8

# # CMPE 256 Programming Assignment 3 - Social Network Analysis
# 
# #### Dataset Used: Wikipidea Vote taken from https://snap.stanford.edu/data/wiki-Vote.html
# 
# #### About the data:
# 
# The network contains all the Wikipedia voting data from the inception of Wikipedia till January 2008. Nodes in the network represent wikipedia users and a directed edge from node i to node j represents that user i voted on user j.
# 
# #### Networkx:
# NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

# ### Load the dataset into networkx using edgelist method and creating a graph

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
import heapq

G=nx.read_edgelist("../data/Wiki-Vote.txt", create_using=nx.DiGraph())
nx.info(G)


# As given in the dataset description, the graph is directed. Hence, I used the nx.DiGraph() function to intialize the graph as a directed one

# ### 1. Number of Nodes in the graph

# In[2]:


nodes= nx.number_of_nodes(G)
print("The number of nodes present in the graph is : " ,nodes)


# ### 2. Number of Edges in the graph

# In[3]:


edges= nx.number_of_edges(G)
print("The number of edges present in the graph is : " ,edges)


# ### 3. Checking if the graph is connected or not and displaying the number of connected components

# #### (a) Checking if the Graph is Connected or not?

# In[4]:


nx.is_strongly_connected(G)


# As we have checked and found that the graph is not strongly connected, let us find the number of connected components in the next step

# #### (b) Finding the Number of Connected Components

# In[5]:


components1= nx.number_weakly_connected_components(G)
print("The number of weakly connected componenets in graph is: ",components1) 

components2 = nx.number_strongly_connected_components(G)
print("The number of strongly connected componenets in graph is: ",components2) 


# In[6]:


strong_con_comp = nx.strongly_connected_components(G)


# ### 4. Diameter (longest shortest path) of the graph

# #### As the graph is strongly connected, the diameter will be infinite.

# ### 5. Average clustering coefficient of the graph

# In[7]:


avg_clus_coeff = nx.average_clustering(G)
print("The average clustering coefficient of the graph is: ",avg_clus_coeff)


# ### 6. Closeness & Betweenness Centralities

# #### (a) Top 5 nodes with the highest closeness centrality

# In[8]:


closeness_centrality = nx.closeness_centrality(G)
type(closeness_centrality)


# The closeness_centrality() of networkx returns a dictionary of the nodes and their closeness centrality values. In the next cell, I used the heapq library of python to get the top 5 nodes with the highest closeness centrality.

# In[9]:


k = heapq.nlargest(5, closeness_centrality, key=closeness_centrality.get)
print("The top 5 nodes having highest closeness centrality are:")
for i in k:
    print("Node:",i)


# #### (b) Top 5 nodes with the highest betweenness centrality

# In[10]:


betweenness_centrality = nx.betweenness_centrality(G)
type(betweenness_centrality)


# The betweenness_centrality() of networkx returns a dictionary of the nodes and their betweenness centrality values. In the next cell, I used the heapq library of python to get the top 5 nodes with the highest betweenness centrality.

# In[11]:


k1 = heapq.nlargest(5, betweenness_centrality, key=betweenness_centrality.get)
print("The top 5 nodes having highest betweenness centrality are:")
for i in k1:
    print("Node:",i)


# ### 7. Dispersion between the two nodes with highest PageRank

# #### Finding PageRank

# In[12]:


pagerank = nx.pagerank(G)
type(pagerank)


# The pagerank() of networkx returns a dictionary of the nodes and their pagerank values. In the next cell, I used the heapq library of python to get the top 2 nodes with the highest pagerank values.

# In[13]:


k2 = heapq.nlargest(2, pagerank, key=pagerank.get)
print("The nodes having highest PageRank are:")
for i in k2:
    print("Node:",i)


# #### Dispersion between the two nodes with highest PageRank

# The dispersion of the two noded can be found by passing them as arguments to the dispersion() function of networkx library.

# In[14]:


dispersion2 = nx.dispersion(G,u="4037",v="15")
print("The dispersion of the two nodes with the highest pageranks is:", dispersion2)


# ### 8. Top Five nodes with the highest authority score according to HITS

# In[15]:


hubs, authority_score = nx.hits(G, normalized=False)
type(authority_score)


# The hits() function of networkx library returns a tuple of hub values and authority scores. The authority scores are in dictionary format, in the next step, by using heapq library, the top 5 nodes with highest authority scores can be found.

# In[16]:


k3 = heapq.nlargest(5, authority_score, key=authority_score.get)
print("The top 5 nodes having highest authority scores according to HITS are:")
for i in k3:
    print("Node:",i)


# ### 9. Communities using the Girvan Newman algorithm

# For finding the communities in the given graph using Girvan Newman Algorithm, we use the girvan_newman() function. <br>
# For this step, I converted the directed graph as an undirected one for feasiblity.

# In[17]:


from networkx.algorithms.community.centrality import girvan_newman
G1 = G.to_directed()
communities = girvan_newman(G1, most_valuable_edge=None)


# In[18]:


type(communities)


# The girvan_newman() function returns a generator format. The generator is an iterator of tuples of sets of nodes in the graph. Each set of node is a community, each tuple is a sequence of communities at a particular level of the algorithm.

# In[19]:


sorted_comm = tuple(sorted(c) for c in next(communities))


# In[20]:


print("By using Girvan Newman algorithm, the number of communities in the given graph are: ",len(sorted_comm))


# ### 10. Top 5 nodes for each community found using Girvan Newman algorithm

# In[23]:


print("The 5 nodes in each community: ")
for i in range(0,len(sorted_comm)):
    print(sorted_comm[i][:5])


# Here, each community has different number of nodes, the minimum community being 2.

# ### Discussions:
# 
# - The dataset contains only 2 columns, FromNodeId and ToNodeId
# - Networkx is used to build the graph and load the edges from the dataset
# - The in built functions of networkx such as closeness_centrality(), betweenness_centrality(), diameter(), pagerank(), hits() are used for the analysis of the graph.
# - Girvan Newman algorithm is used to find the communities in the graph

# ### References:
# 
# - https://networkx.github.io/documentation/stable/index.html
# 
