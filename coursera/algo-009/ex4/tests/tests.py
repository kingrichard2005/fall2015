import os
import unittest
import FileLoader
import copy
import sys
from FileLoader import FileLoader

class Ex4Tests(unittest.TestCase):
  def test_file_loader_can_load_list_of_x_y_edges_as_2tuples(self):
    edge_list      = os.path.join(os.path.dirname(__file__), "sample_files", "SCC.txt")
    result         = FileLoader.compute_scc_from_edge_list(edge_list)
    self.assertTrue(len(result) > 0)

if __name__ == '__main__':
	unittest.main()