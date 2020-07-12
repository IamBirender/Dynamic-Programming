class Solution(object):
    def __init__(self):
        self.dp = list()
        self.main_list = list()
    
    def count_subset(self, array, sum):
        N = len(array)
        result_recursion = self._recursion(array, sum, N, [])
        print(self.main_list)
        print(result_recursion)

    def _recursion(self, array, sum,N, sublist):
        if N == 0 :
            return False
        if sum == 0:
            if len(sublist):
                self.main_list + [sublist]
                print(self.main_list, "hello")
            return True

        print(array[N-1], sublist, sum)
        if array[N-1] <= sum:
            return self._recursion(array, sum, N-1, sublist) or self._recursion(array, sum - array[N-1], N-1, sublist + [array[N-1]])
        else:
            return self._recursion(array, sum, N-1, sublist)

    def _recursion_memoization(self, array, sum):
        pass

    def _top_down(self, array, sum):
        pass

array = [2,3,5,6,8,10]
sum = 10
solution = Solution()
print(solution.count_subset(array, sum))
