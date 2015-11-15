import  csv
__author__ = 'kingrichard2005'

class FileLoader(object):
  @staticmethod
  def compute_scc_from_edge_list(inFile):
    import networkx as nx
    print "building a NetworkX DiGraph..."
    networkx_digraph = nx.DiGraph()
    with open(inFile,'rbU') as f:
      for row in f:
        inputstr  = row.split()
        list_tmp  = [int(inputstr[0]), int(inputstr[1])]
        tuple_tmp = (int(inputstr[0]), int(inputstr[1]))
        networkx_digraph.add_nodes_from(list_tmp)
        networkx_digraph.add_edges_from([tuple_tmp])
    print "computing NetworkX DiGraph's strongly_connected components..."
    scc_list = [len(c) for c in sorted(nx.strongly_connected.strongly_connected_components(networkx_digraph), key=len, reverse=True)]
    return scc_list