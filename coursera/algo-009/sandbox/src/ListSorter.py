class ListSorter(object):
    @staticmethod
    def CountInversionsSimpleMethod( arr, int_n ):
        '''
            Python version of C implementation
            http://www.geeksforgeeks.org/counting-inversions/
        '''
        inv_count = 0;
        for i in range(0, int_n - 1):
            for j in range(i+1, int_n):
                if arr[i] > arr[j]:
                    inv_count += 1;
        return inv_count;
    
    @staticmethod
    def MergeSortList(A):
        '''
        From lecture notes
        ref:
        http://www.cp.eng.chula.ac.th/~piak/teaching/algo/algo2008/count-inv.htm
        '''
        l = len(A)
        if l > 1:
            # use integer / floor division to get a valid index
            n = l//2
            C = A[:n]
            D = A[n:]
            C, c = ListSorter.MergeSortList(A[:n])
            D, d = ListSorter.MergeSortList(A[n:])
            B, b = ListSorter.MergeAndCountInversions(C,D)
            return B, b+c+d
        else:
            return A, 0

    @staticmethod
    def MergeAndCountInversions(A,B):
        '''
        While merging elements in arrays 'A' and 'B', count number of 
        inversions.  An inversion occurs when the head element in 'A' 
        is greater than the head element in 'B'
        '''
        inversion_count = 0L
        M = []
        # Merge and count while A and B are not empty
        while A and B:
            M.append( min(A[0], B[0]) )
            if A[0] <= B[0]:
                A.pop(0)
            else:
                inversion_count += len(A)
                B.pop(0)
        M  += A + B
        return M, inversion_count