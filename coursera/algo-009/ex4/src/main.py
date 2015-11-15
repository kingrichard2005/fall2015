__author__ = 'kingrichard2005'
import os
import FileLoader
import copy
import sys
import argparse
from FileLoader import FileLoader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="SCC"
                                           ,description='Computes strongly connected components from edge list')
    parser.add_argument('-f', '--file'
                          ,help='Edge list'
                          ,dest="my_edge_list");

    args = parser.parse_args();
    scc_list         = FileLoader.compute_scc_from_edge_list(args.my_edge_list)
    for component in scc_list:
      print "{0}".format(component)