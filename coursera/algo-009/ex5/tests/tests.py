import os
import unittest
import FileLoader
import Djikstra
import copy
import sys
from FileLoader import FileLoader
from Djikstra import Djikstra

class Ex4Tests(unittest.TestCase):
  def test_file_loader(self):
    inputfile = os.path.join(os.path.dirname(__file__), "sample_files", "dijkstraData.txt")
    result      = FileLoader.load_adjacency_list(inputfile)
    self.assertTrue(len(result) > 0)

  def test_compute_djikstra_shortest_path(self):
    inputfile                 = os.path.join(os.path.dirname(__file__), "sample_files", "dijkstraData.txt")
    undirected_weighted_graph = FileLoader.load_adjacency_list(inputfile)
    result                    = Djikstra.compute_shortest_path(undirected_weighted_graph)
    result_str                = ""
    for ind in [7,37,59,82,99,115,133,165,188,197]:
        result_str = result_str + str(ind) + ':' + str(result[ind]) + "\n"
    self.assertTrue(len(result) > 0)

if __name__ == '__main__':
	unittest.main()