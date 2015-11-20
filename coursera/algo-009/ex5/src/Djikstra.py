
class Djikstra(object):
  @staticmethod
  def compute_shortest_path(source_vertex = 1, undirected_weighted_graph = {}):
    total_vertices      = len(undirected_weighted_graph.keys())
    vertices_visited    = [source_vertex]
    vertices_notvisited = list(range( 2, total_vertices + 1))
    distances           = {x:0 for x in range( 1, total_vertices + 1 )}
    iter_limit          = 1000000

    while len(vertices_visited) <  total_vertices:
        tmpdist = iter_limit
        lenvw   = tmpdist
        for v in vertices_visited:
            for w in vertices_notvisited:
                tmpKeys = undirected_weighted_graph[v].keys()
                if w in tmpKeys:
                    lenvw = distances[v] + undirected_weighted_graph[v][w]
                    if lenvw < tmpdist:
                        tmpdist = lenvw
                        tmpv    = v
                        tmpw    = w

        if tmpdist == iter_limit:
            break
        vertices_visited.append(tmpw)
        vertices_notvisited.remove(tmpw)
        distances[tmpw] = tmpdist

    return distances