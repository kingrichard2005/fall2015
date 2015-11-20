import csv
__author__ = 'kingrichard2005'

class FileLoader(object):
  @staticmethod
  def load_adjacency_list(inFile):
    vertices = {}
    with open(inFile,'rbU') as f:
      for row in f:
        inputstr              = row.split();
        key                   = int(inputstr[0])
        neighbor_weight_pairs = { int(x.split(',')[0]) : int(x.split(',')[1]) for x in inputstr[1:] }
        vertices[key]         = neighbor_weight_pairs
    return vertices