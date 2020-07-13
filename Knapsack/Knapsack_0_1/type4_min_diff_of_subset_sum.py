class Solution(object):
    def __init__(self):
        self.dp = list()

    def min_diff_subsets(self, array):
        N = len(array)
        range = sum(array)
        agg = range//2
        result = self._recursion(array, N, agg)
        print(range - 2*(agg-result))
        return range - 2*agg
    
    def _recursion(self, array, N, agg):
        if N == 0 :
            return agg
        if agg == 0:
            return agg
        if array[N-1] <= agg:
            return min(self._recursion(array, N-1, agg - array[N-1]), self._recursion(array, N-1, agg))
        else:
            return self._recursion(array, N-1, agg)
        

array = [1000,1,1,1,1]
solution = Solution()
solution.min_diff_subsets(array)  


