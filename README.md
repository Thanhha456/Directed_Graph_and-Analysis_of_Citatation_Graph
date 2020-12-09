## Assessment:**Degree Distributions for Graphs and Analysis of Citation Graphs**

**Firts part:** Write Python code that creates dictionaries corresponding to some simple examples of graphs.
You will also implement two short functions that compute information about the distribution of the in-degrees for nodes in these graphs

**Second part:** Implement two functions that compute the distribution of the in-degrees of the nodes of a directed graph.

**Third part:** Analyze a real-world problem: How do scientific papers get cited?
- Your task is to load a provided citation graph for 27,770 high energy physics theory papers. This graph has 352,768 edges.
You should use the following code to load the citation graph as a dictionary
CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"
Compute the in-degree distribution for this citation graph. Once you have computed this distribution,
you should normalize the distribution (make the values in the dictionary sum to one) and then compute a log/log plot of the points in this normalized distribution.
- Generate random directed graphs: For every ordered pair of distinct nodes (i,j), the modified algorithm adds the directed edge from i to j with probability p.
Consider the shape of the in-degree distribution for an ER graph and compare its shape to that of the physics citation graph.
- Create a complete directed graph on m nodes. Then, the algorithm grows the graph by adding n−m nodes, where each new node is connected to m nodes randomly
chosen from the set of existing nodes. As an existing node may be chosen more than once in an iteration,
we eliminate duplicates (to avoid parallel edges); hence, the new node may be connected to fewer than m existing nodes upon its addition.
For this question, we will choose values for n and m that yield a DPA graph whose number of nodes and edges is roughly the same to those of the citation graph.
http://www.codeskulptor.org/#alg_dpa_trial.py
For the nodes, choosing n to be the number of nodes as the citation graph is easy.
Since each step in the DPA algorithm adds m edges to the graph, a good choice for m is an integer that is close to the average out-degree of the physics citation graph.
Compute a DPA graph, and then plot the in-degree distribution for this DPA graph. Compute a (normalized) log/log plot of the points in the graph's in-degree distribution
- Compare the in-degree distribution for the citation graph to the in-degree distribution for the DPA graph. You should consider the following three phenomena:
    The "six degrees of separation" phenomenon,
    The "rich gets richer" phenomenon, and
    The "Hierarchical structure of networks" phenomenon.

**Outcomes:**
- The plot on log/log scale of the Citograph shows the linear tendention of the in_degree distribution with a negative slope to the rise of the in_degree, which is content to the reality that vas of papers are rarely citated only the most popular papers get mentioned  mostly, and they are very much at small fractions.
- ER graph, which is randomly generated has a bell_shape in_degree distribution, means all the nodes are with the same probablity get connected, the expected value of the in_degree is the same for every node.Most of nodes have the same number of edges.
- DPA graph that generated according to the DPA algorithm has the same maner as the Citograph with a decline linear slope with the rise of the in_degree. The nodes that have higher in_degree( lot of citations) are more likely to get new edges( due to the higher visiblity). This characteristic behavior correspondens to the "rich gets richer" phenomen, the most popular newspers, get read more, the best artists get often mentioned, the rich people get more chances in bussines to get richer.  
