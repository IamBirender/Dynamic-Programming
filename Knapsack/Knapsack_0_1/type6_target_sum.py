class Solution(object):
    def __init__(self, array, diff):
        self.array = array
        self.N = len(array)
        self.arr_total = sum(array)
        self.given_diff = diff

    def count_diff_subsets(self):
        return self._hypothesis(self.array, self.N, 0)
    
    def _hypothesis(self, array, N, subset_sum):
        if N == 0:
            delta = abs(2*subset_sum - self.arr_total)
            if delta == self.given_diff:
                return True
            return False

        return self._hypothesis(array[:-1], N-1, subset_sum + array[-1]) or self._hypothesis(array[:-1], N-1, subset_sum ) 
        


array = [1,6,11,5]
diff = 21
solution = Solution(array, diff)
print(solution.count_diff_subsets()) 


