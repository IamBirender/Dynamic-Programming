class Solution(object):
    def __init__(self):
        pass
    def findsubset(self, arr, sum):
        N = len(arr)
        result = self._recursive_solution(arr, sum, N)
        print(result)
        return result

    def _recursive_solution(self, arr, sum, N):
        # writing the base condition - think about the smallest valid input
        if sum == 0:
            return True 

        if N == 0:
            return False
        if arr[N-1] <= sum:
            return self._recursive_solution(arr, sum-arr[N-1], N-1) or self._recursive_solution(arr, sum, N-1)
        else:
            return self._recursive_solution(arr, sum, N-1)
        
arr = [2,3,7,8,10]
sum = 11

new = Solution()
new.findsubset(arr, sum)
