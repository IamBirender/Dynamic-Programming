class solution(object):
    def __init__(self, coin_array, coin_sum):
        self.coin_array = coin_array
        self.coin_sum = coin_sum
        self.N = len(coin_array)
        self.memo = [[-1 for i in range(self.coin_sum+1)] for j in range(self.N+1)]
        self.dp = [[0 for i in range(self.coin_sum+1)] for j in range(self.N+1)]
        
    def _get_coins(self):
#         return self.__recursive_way(self.coin_array, self.coin_sum)
#         return self.__rec_with_memo(self.N,self.coin_sum)
        return self.__dp_solution()
    
    
    def __recursive_way(self, arr, net):
        if len(arr) == 0 or net == 0:
            if net == 0:
                return 1
            else:
                return 0
        
        if arr[-1] <= net:
            return self.__recursive_way(arr, net-arr[-1]) + self.__recursive_way(arr[:-1], net)
        else:
            return self.__recursive_way(arr[:-1], net)
    
    def __rec_with_memo(self, n, s):
        if n == 0 or s == 0:
            if s == 0:
                return 1
            else:
                return 0
        
        if self.memo[n][s] != -1:
            return self.memo[n][s]
        
        if self.coin_array[n-1] <= s:
            self.memo[n][s] = self.__rec_with_memo(n, s-self.coin_array[n-1]) + self.__rec_with_memo(n-1, s)
        else:
            self.memo[n][s] = self.__rec_with_memo(n-1, s)
        
        return self.memo[n][s]
    
    def __dp_solution(self):
        for i in range(self.N+1):
            for j in range(self.coin_sum+1):
                if j == 0:
                    self.dp[i][j] = 1
                elif i == 0:
                    self.dp[i][j] = 0 
                elif self.coin_array[i-1] <= j:
                    self.dp[i][j] = self.dp[i][j-self.coin_array[i-1]] + self.dp[i-1][j]
                else:
                    self.dp[i][j] = self.dp[i-1][j]
        return self.dp[-1][-1]
        
coin = [1,2,3]
total = 5
obj = solution(coin, total)
print(obj._get_coins())
