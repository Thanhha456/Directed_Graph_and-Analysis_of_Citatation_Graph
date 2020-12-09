# This is a sample Python script.
"""
Firts part: Write Python code that creates dictionaries corresponding to some simple examples of graphs.
You will also implement two short functions that compute information about the distribution of the in-degrees for nodes in these graphs
Second part: Implement two functions that compute the distribution of the in-degrees of the nodes of a directed graph.
Third part: analyze a real-world problem: How do scientific papers get cited?
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
"""
CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"
import urllib.request as urllib2
import math
import random
import matplotlib.pyplot as plt
import alg_dpa_trial
STANDARD = False

EX_GRAPH0 = {0: set([1, 2]),
             1: set(),
             2: set()}
EX_GRAPH1 = {0: set([1, 5, 4]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set()}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set(),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 4, 5, 6, 7, 3])}

def make_complete_directed_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with the specified number of nodes.
    """
    digraph = {}
    for num_x in range(num_nodes):
        val = set()
        for num_y in range(num_nodes):
            if num_x != num_y:
                val.add(num_y)
        digraph[num_x] = val
    return digraph

def compute_indegrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph.
    The function should return a dictionary with the same set of keys (nodes) as digraph whose corresponding values are
    the number of edges whose head matches a particular node.
    :param digraph:
    :return:
    """
    keys = list(digraph.keys())
    degree_dic = {}
    for key in keys:
        count = 0
        for val_set in list(digraph.values()):
            for val in val_set:
                if val == key:
                    count += 1
        degree_dic[key] = count
    return degree_dic

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution of the in-degrees of the graph.
    The function should return a dictionary whose keys correspond to in-degrees of nodes in the graph.
    The value associated with each particular in-degree is the number of nodes with that in-degree.
    In-degrees with no corresponding nodes in the graph are not included in the dictionary.
    """
    distribution = {}
    degree = compute_indegrees(digraph)
    values = list(degree.values())
    for dummy_val in values:
        if dummy_val != 0:
            distribution[dummy_val] = values.count(dummy_val)
    return distribution

###################################
# Code for loading citation graph
def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.decode().split('\n')
    graph_lines = graph_lines[: -1]

    print("Loaded graph with", len(graph_lines), "nodes")

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph
def normalized_distribution(digraph):
    """
    Compute normalize the distribution (make the values in the dictionary sum to one) and
    then compute a log/log plot of the points in this normalized distribution.
    """
    distribution = in_degree_distribution(digraph)
    sum_degrees = sum(list(distribution.values()))
    norm_dist = {}
    # graph = {"name1":"CITATION GRAPH","name2": "ER GRAPH", "name3": "DPA GRAPH"}

    if not STANDARD:
        for dummy in list(distribution.keys()):
            norm_dist[math.log(dummy)] = math.log(distribution[dummy] / sum_degrees)
    else:
        for dummy in list(distribution.keys()):
            norm_dist[dummy] = distribution[dummy] / sum_degrees
    #build plots
    plt.scatter(list(norm_dist.keys()), list(norm_dist.values()))

    if STANDARD:
        plt.xlabel("in_degree")
        plt.ylabel("fraction of nodes")
        plt.title("In_degree distribution (log/log plot) of the Citograph graph 27770 nodes")
    else:
        plt.xlabel("in_degree")
        plt.ylabel("fraction of nodes")
        plt.title("In_degree distribution (log/log plot) of the Citograph graph 27770 nodes")
    plt.show()
def er_graph(num_nodes, p):
    """
    Generate random directed graphs: For every ordered pair of distinct nodes (i,j),
    the modified algorithm adds the directed edge from i to j with probability p.
    """
    digraph = {}
    for num_x in range(num_nodes):
        val = set()
        for num_y in range(num_nodes):
            if num_x != num_y:
                if random.random() <= p:
                    val.add(num_y)
        digraph[num_x] = val
    print("Generated graph with", len(digraph), "nodes")
    return digraph
def define_m(digraph):
    """
    For the nodes, choosing n to be the number of nodes as the citation graph is easy.
    Since each step in the DPA algorithm adds m edges to the graph, a good choice for m is
    an integer that is close to the average out-degree of the physics citation graph.
    """
    #define out_degree of each node
    out_degrees = {}
    for node in digraph:
        out_degree = len(digraph[node])
        out_degrees[node] = out_degree
    tot_out_degr = sum(list(out_degrees.values()))
    ave_out_degr = math.ceil(tot_out_degr/len(digraph))
    return ave_out_degr

def dpa_graph(num_nodes, m):
    """
    Generate a random directed graph num_nodes, m (m≤n), which is the number of existing nodes to which a new node is connected during each iteration. Notice that m is fixed throughout the procedure.
     Then, the algorithm grows the graph by adding n−m nodes, where each new node is connected to m nodes randomly
    chosen from the set of existing nodes. As an existing node may be chosen more than once in an iteration,
    we eliminate duplicates (to avoid parallel edges); hence, the new node may be connected to fewer than m existing nodes upon its addition.
    For this question, we will choose values for n and m that yield a DPA graph whose number of nodes and edges is roughly the same to those of the citation graph.
    """
    #Generate a random directed graph num_nodes, m (m≤n)
    digraph = make_complete_directed_graph(m)
    graph = alg_dpa_trial.DPATrial(m)
    for dummy in range(m, num_nodes):
        digraph[dummy] = graph.run_trial(m)
    return digraph

# citation_graph = load_graph(CITATION_URL)
# m =define_m(citation_graph)
# m = 13
# print(in_degree_distribution(EX_GRAPH1))
# print(make_complete_graph(3))
# print(compute_in_degrees(EX_GRAPH1))
# num_nodes = 27770
# p = .3
# num_nodes = 10
# digraph = er_graph(num_nodes, p)
# digraph = dpa_graph(num_nodes, m)
# print(digraph)
# normalized_distribution(citation_graph)