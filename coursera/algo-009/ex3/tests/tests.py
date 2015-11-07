import os
import unittest
import FileLoader
import kargerMinCut
import copy
from FileLoader import FileLoader
from kargerMinCut import kargerMinCut

class Ex3Tests(unittest.TestCase):

	def test_file_loader_can_load_list_of_integers(self):
		# arrange
		adjacency_list = os.path.join(os.path.dirname(__file__), "sample_files", "kargerMinCut.txt")
		# act
		result = FileLoader.load_adjacency_map(adjacency_list)
		# assert
		self.assertTrue(len(result) > 0)

	def test_find_minimum_cut(self):
		# arrange
		adjacency_list = os.path.join(os.path.dirname(__file__), "sample_files", "kargerMinCut.txt")
		adjacency_map  = FileLoader.load_adjacency_map(adjacency_list)
		# act
		global_minimum_cut =  kargerMinCut.edge_contraction(copy.deepcopy(adjacency_map)) 
		#looping for sample
		for i in range(1, 200):
			this_min_cut = kargerMinCut.edge_contraction(copy.deepcopy(adjacency_map))	
			if this_min_cut < global_minimum_cut:
				global_minimum_cut = this_min_cut

			print "iteration {}: minimum cut is {}".format(i,global_minimum_cut)
		# assert
		self.assertTrue(global_minimum_cut > 0)

if __name__ == '__main__':
	unittest.main()