import random
import copy

class kargerMinCut(object):

	# Use a dictionary / map to model each nodes adjacency list
	@staticmethod
	def randomEdge(adjacency_map):
		vertex1 = adjacency_map.keys()[random.randint(0, len(adjacency_map)-1)]
		vertex2 = adjacency_map[vertex1][random.randint(0, len(adjacency_map[vertex1])-1)]
		return vertex1, vertex2

	#Karger's edge contraction min cut algorithm
    # "https://en.wikipedia.org/wiki/Karger%27s_algorithm#Contraction_algorithm"
	@staticmethod
	def edge_contraction(adjacency_map):
		while len(adjacency_map) > 2:
            # random edge selection
			vertex1, vertex2 = kargerMinCut.randomEdge(adjacency_map)
			# extend vertex1 adjacency list with vertex2 adjacency list
			adjacency_map[vertex1].extend(adjacency_map[vertex2])
			this_vertex = []
			# edge contraction procedure
			for entry in adjacency_map[vertex2]:
				this_vertex = adjacency_map[entry]
				for i in range(0, len(this_vertex)):
					if this_vertex[i] == vertex2:
						this_vertex[i] = vertex1
				adjacency_map[entry] = this_vertex	
		
			# remove vertex1 self loops
			while vertex1 in adjacency_map[vertex1]:
				adjacency_map[vertex1].remove(vertex1)
			
			# remove vertex2 entry from adjacency map
			del adjacency_map[vertex2]

		return len(adjacency_map[adjacency_map.keys()[1]])
