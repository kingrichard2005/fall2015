__author__ = 'kingrichard2005'
import ListSorter
import FileLoader
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="count_inversions"
                                         ,description='(Merge) sorts a list of ints and counts the total number of inversions')
    parser.add_argument('-f', '--file'
                            ,help='File list of ints to be sorted'
                            ,dest="my_file_list");
    args = parser.parse_args();
    input = FileLoader.FileLoader.load_list_of_long_integers(args.my_file_list)
    my_sorted_list, count = ListSorter.ListSorter.MergeSortList(input)
    #print "Sorted list is: ", my_sorted_list
    print "Total number  of inversions: ", count
