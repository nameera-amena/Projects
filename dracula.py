# Student name(s):  Nameera Amena
# Student ID(s):  22226730
 
import sys
import itertools
import networkx as nx

def read_combinations(input_file_name):
    with open(input_file_name) as data:
        dictionary = eval(data.read())
    Combinations_soc_list=[]
    for v in dictionary.values():
       Combinations_soc_list.extend(list(itertools.combinations(v,2)))
    return(Combinations_soc_list)
        
G = nx.Graph()
edges=read_combinations(sys.argv[1])
G.add_edges_from(edges)

def Finding_path(G,source,target):
    if not nx.has_path(G,source,target):
        raise RuntimeError(f"No path found between {source} and {target}")
    path = nx.dijkstra_path(G,source,target)
    return(path)

print(Finding_path(G,"Dracula","Pumpkin"))