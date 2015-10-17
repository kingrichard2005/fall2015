import os
import unittest
import FileLoader
import ListSorter
from FileLoader import FileLoader
from ListSorter import ListSorter

class HW1Tests(unittest.TestCase):

    def test_file_loader_can_load_list_of_integers(self):
        # arrange
        fn_list_of_integers = os.path.join(os.path.dirname(__file__), "sample_files", "IntegerArray.txt")
        # act
        result = FileLoader.load_list_of_long_integers(fn_list_of_integers)
        # assert
        self.assertTrue(len(result) > 0)

    def test_merge_count_inversions(self):
        # arrange
        aFile = os.path.join(os.path.dirname(__file__), "sample_files", "IntegerArray.txt")
        list_of_integers = FileLoader.load_list_of_long_integers(aFile)
        A = list_of_integers[0:3]
        B = list_of_integers[4:7]
        # act
        merged_result, inversion_count = ListSorter.MergeAndCountInversions(A, B)
        # assert
        self.assertTrue(len(merged_result) > 0 and inversion_count > 0)

    def test_merge_sorting_list(self):
        # arrange
        A = [2, 4, 1, 3, 5]
        # act
        merged_result, inversion_count = ListSorter.MergeSortList(A)
        # assert
        self.assertTrue(inversion_count == 3L)

if __name__ == '__main__':
    unittest.main()