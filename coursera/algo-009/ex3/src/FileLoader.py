import  csv
__author__ = 'kingrichard2005'

class FileLoader(object):
	@staticmethod
	def load_adjacency_map(inFile):
		"""
		Load a text file
		"""
		vertex_map = {}
		for line in open(inFile,'rbU').readlines():	
			a_line_item   = []
			a_line_item   = line.split()
			x             = a_line_item.pop(0)
			vertex_map[x] = a_line_item
		return vertex_map;