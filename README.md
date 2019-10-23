# Social Network Analysis Example

This is an example of social network analysis. 

### Data Description
Dataset Used: Wikipidea Vote taken from https://snap.stanford.edu/data/wiki-Vote.html

#### About data:

The network contains all the Wikipedia voting data from the inception of Wikipedia till January 2008. Nodes in the network represent wikipedia users and a directed edge from node i to node j represents that user i voted on user j.

### Networkx:
NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

### Tasks
The following tasks are performed on the dataset.

1.  Finding Number of nodes.
2.  Finding Number of edges.
3. a) Is the graph connected?<br>
   b) If not, return number of connected components.
4.  The diameter of the graph (longest shortest path).
5. The average clustering coefficient of the graph.
6.  a)  The five nodes with the highest closeness centrality<br>
    b) The five nodes with the highest betweeness centrality
7. The dispersion between the two nodes with highest PageRank
8. The five nodes with the highest authority score according to HITS
9. Find the communities using the Girvan Newman algorithm. Print the number of communities
10. (cont'd from 9) Print the top-5 nodes for each community you found in step 9.
