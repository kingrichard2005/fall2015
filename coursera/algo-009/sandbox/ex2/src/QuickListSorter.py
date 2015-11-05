class QuickListSorter(object):
    
    @staticmethod
    def is_median_elemet(a,b,c):
        return True if (( a <= b <= c ) or (c <= b <= a )) else False

    @staticmethod
    def quicksort_with_first_as_pivot(A,begin,end):
        count = 0
        if end - begin <= 1:
            return 0
        else :
            split = QuickListSorter.partition(A,begin,end)
            count = end - begin - 1
            lc    = QuickListSorter.quicksort_with_first_as_pivot(A,begin,split)				
            rc    = QuickListSorter.quicksort_with_first_as_pivot(A,split+1,end)
            return count + lc + rc
    
    @staticmethod
    def quicksort_with_last_as_pivot(A,begin,end):
        count = 0
        if end - begin <= 1:
            return 0
        else :
            # Since element at A[begin] is used as the pivot just swap 
            # first and the last so last is used as the pivot instead
            A[begin], A[end-1] = A[end-1] , A[begin]
            split = QuickListSorter.partition(A,begin,end)
            count = end - begin - 1
            lc    = QuickListSorter.quicksort_with_last_as_pivot(A,begin,split)				
            rc    = QuickListSorter.quicksort_with_last_as_pivot(A,split+1,end)
            return count + lc + rc

    @staticmethod
    def quicksort_with_median_of_three_as_pivot(A,begin,end):
        count = 0
        if end - begin <= 1:
            return 0
        else :
            med = begin + (end - begin + 1)/2 - 1

            if QuickListSorter.is_median_elemet(A[begin],A[med],A[end-1]) :
                A[begin], A[med] = A[med] , A[begin]
            elif QuickListSorter.is_median_elemet(A[begin],A[end-1],A[med]) :
                A[begin], A[end-1] =  A[end-1], A[begin]

            split = QuickListSorter.partition(A,begin,end)
            count = end - begin - 1
            lc    = QuickListSorter.quicksort_with_median_of_three_as_pivot(A,begin,split)				
            rc    = QuickListSorter.quicksort_with_median_of_three_as_pivot(A,split+1,end)
            return count + lc + rc
    
    @staticmethod
    def partition(A,begin,end):
        pivot = A[begin]
        i     = begin + 1

        for j in range(begin+1,end):
            if A[j] < pivot :					
                A[i], A[j] = A[j], A[i]
                i += 1
        
        A[i-1], A[begin] = A[begin], A[i-1]
        return i-1