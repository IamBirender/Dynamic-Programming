class Solution(object):
    def __init__(self):
        self.dp = list()
        self.main_list = list()
    
    def count_subset(self, array, sum):
        N = len(array)
        result_recursion = self._recursion(array, sum, N)
        print(result_recursion)
        self.dp = [[-1 for i in range(sum +1)] for j in range(N+1)]
        result_memoize = self._recursion_memoization(array, sum, N)
        print(result_memoize)
        result_top_down = self._top_down(array, sum, N)
        print(result_top_down)

    def _recursion(self, array, sum, N):
        if sum == 0:
            return 1
        if N == 0 :
            return 0
        if array[N-1] <= sum:
            return self._recursion(array, sum, N-1) + self._recursion(array, sum - array[N-1], N-1)
        else:
            return self._recursion(array, sum, N-1)

    def _recursion_memoization(self, array, sum, N):
        if sum == 0:
            return 1
        if N == 0 :
            return 0
        if self.dp[N-1][sum] != -1:
            return self.dp[N-1][sum]
        else:
            if array[N-1] <= sum:
                self.dp[N-1][sum] = self._recursion(array, sum, N-1) + self._recursion(array, sum - array[N-1], N-1)
                return self.dp[N-1][sum]
            else:
                self.dp[N-1][sum] = self._recursion(array, sum, N-1)
                return self.dp[N-1][sum]

    def _top_down(self, array, sum, N):
        for i in range(N + 1):
            for j in range(sum+1):
                if j == 0:
                    self.dp[i][j] = 1
                elif i == 0:
                    self.dp[i][j] = 0
                elif array[i-1] <= j:
                    self.dp[i][j] = self.dp[i-1][j-array[i-1]] + self.dp[i-1][j]
                else:
                    self.dp[i][j] = self.dp[i-1][j]
        return self.dp[N][sum]

array = [2,3,5,6,8,10]
sum = 10
solution = Solution()
solution.count_subset(array, sum)
