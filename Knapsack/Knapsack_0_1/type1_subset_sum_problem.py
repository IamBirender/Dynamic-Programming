import time 
class Solution(object):
    def __init__(self):
        self.dp = list()

    def findsubset(self, arr, sum):
        N = len(arr)
        self.dp = [[False for i in range(sum+1)] for j in range(N+1)] 
        a = time.perf_counter()
        result = self._recursive_solution(arr, sum, N)
        b = time.perf_counter()
        result = self._rec_with_memoization(arr, sum, N)
        c = time.perf_counter()
        result = self._top_down(arr, sum, N)
        d = time.perf_counter()
        print("rec without memo :" ,b-a , "time_with memo : ",c-b," top_down : ", d-c )
        return result

    def _recursive_solution(self, arr, sum, N):
        if sum == 0:
            return True 
        if N == 0:
            return False
        if arr[N-1] <= sum:
            return self._recursive_solution(arr, sum-arr[N-1], N-1) or self._recursive_solution(arr, sum, N-1)
        else:
            return self._recursive_solution(arr, sum, N-1)
    
    def _rec_with_memoization(self, arr, sum, N):
        if sum == 0:
            return True 
        if N == 0:
            return False
        if self.dp[N-1][sum] != -1:
            return self.dp[N-1][sum]

        if arr[N-1] <= sum:
            self.dp[N-1][sum] = self._recursive_solution(arr, sum-arr[N-1], N-1) or self._recursive_solution(arr, sum, N-1)
            return self.dp[N-1][sum]
        else:
            self.dp[N-1][sum] = self._recursive_solution(arr, sum, N-1)
            return self.dp[N-1][sum]
    
    def _top_down(self, arr, sum, N):
        for i in range(N+1):
            for j in range(sum+1):
                if i == 0:
                    self.dp[i][j] = False
                elif j == 0:
                    self.dp[i][j] = True
                elif arr[i-1] <= j:
                    self.dp[i][j] = self.dp[i-1][j-arr[i-1]] or self.dp[i-1][j]
                else:
                    self.dp[i][j] = self.dp[i-1][j]

        return self.dp[N][sum]
    

        
arr = [2,3,7,8,10]
sum = 11

new = Solution()
new.findsubset(arr, sum)
