import os
import unittest
import FileLoader
import QuickListSorter
from FileLoader import FileLoader
from QuickListSorter import QuickListSorter

class Ex2Tests(unittest.TestCase):

    def test_file_loader_can_load_list_of_integers(self):
        # arrange
        fn_list_of_integers = os.path.join(os.path.dirname(__file__), "sample_files", "QuickSort.txt")
        # act
        result = FileLoader.load_list_of_long_integers(fn_list_of_integers)
        # assert
        self.assertTrue(len(result) > 0)

    def test_quick_sort_with_first_as_pivot(self):
        # arrange
        aFile = os.path.join(os.path.dirname(__file__), "sample_files", "QuickSort.txt")
        list_of_integers = FileLoader.load_list_of_long_integers(aFile)
        # act
        result = QuickListSorter.quicksort_with_first_as_pivot(list_of_integers,0,len(list_of_integers))
        # assert
        self.assertTrue(result > 0)

    def test_quick_sort_with_last_as_pivot(self):
        # arrange
        aFile = os.path.join(os.path.dirname(__file__), "sample_files", "QuickSort.txt")
        list_of_integers = FileLoader.load_list_of_long_integers(aFile)
        # act
        result = QuickListSorter.quicksort_with_last_as_pivot(list_of_integers,0,len(list_of_integers))
        # assert
        self.assertTrue(result > 0)

    def test_quick_sort_with_median_of_three_as_pivot(self):
        # arrange
        aFile = os.path.join(os.path.dirname(__file__), "sample_files", "QuickSort.txt")
        list_of_integers = FileLoader.load_list_of_long_integers(aFile)
        # act
        result = QuickListSorter.quicksort_with_median_of_three_as_pivot(list_of_integers,0,len(list_of_integers))
        # assert
        self.assertTrue(result > 0)

if __name__ == '__main__':
    unittest.main()