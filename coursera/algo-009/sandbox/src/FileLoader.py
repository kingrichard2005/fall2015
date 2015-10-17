import  csv
__author__ = 'rgalvan'

class FileLoader(object):
    @staticmethod
    def load_list_of_long_integers(inFile):
        """
        Load a text file
        """
        myListofInts = []
        with open(inFile, mode='rbU') as content:
            for line in content:
                myListofInts.append(long(line.strip()))
        return myListofInts