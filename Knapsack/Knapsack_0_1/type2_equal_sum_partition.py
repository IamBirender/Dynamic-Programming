class Solution(object):
    def __init__(self):
        self.dp = list()
        
    def equal_sum_partition(self, arr):
        agg = sum(arr)
        N = len(arr)
        if agg%2 == 0:
            agg = agg//2
        else:
            return False
        self.dp = [[-1 for i in range(agg+1)] for j in range(N+1)] 
        result = self._recursion(arr, agg, N)
        result_memo = self._recursion_with_memoization(arr, agg, N)
        result_top_down = self._top_down(arr, agg, N)
        return result_top_down

    def _recursion(self, arr, total, N):
        if N == 0:
            return False
        if total == 0:
            return True
        
        if arr[N-1] <= total:
            return self._recursion(arr, total - arr[N-1], N-1) or self._recursion(arr, total, N-1)
        else:
            return self._recursion(arr, total, N-1)
    
    def _recursion_with_memoization(self, arr, total, N):
        if N == 0:
            return False
        if total == 0:
            return True
        if self.dp[N-1][total] != -1:
            return self.dp[N-1][total]
        else:
            if arr[N-1] <= total:
                return self._recursion(arr, total - arr[N-1], N-1) or self._recursion(arr, total, N-1)
            else:
                return self._recursion(arr, total, N-1)

    def _top_down(self, arr, total, N):
        for i in range(N+1):
            for j in range(total+1):
                if i == 0 :
                    self.dp[i][j] = False
                elif j == 0:
                    self.dp[i][j] = True
                elif arr[i-1] <= j:
                    self.dp[i][j] = self.dp[i-1][j-arr[i-1]] or self.dp[i-1][j]
                else:
                    self.dp[i][j] = self.dp[i-1][j]  
        return self.dp[N][total]


arr = [1, 5, 11, 5]
solution = Solution()
print(solution.equal_sum_partition(arr))