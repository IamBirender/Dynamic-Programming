class video_5(object):
    def __init__(self, weight, capacity, value):
        self.weight = weight
        self.capacity = capacity
        self.value = value
        self.N = len(weight)
        self.dp = [[-1 for i in range(capacity+1)] for j in range(self.N+1)]
    
    def _get_highest_profit(self):
        self.__top_down_approach()
        for l in self.dp:
            print(l)
    
    def __top_down_approach(self):
        for i in range(self.N+1):
            for j in range(self.capacity+1):
                if i == 0:
                    self.dp[i][j] = 0
                elif j == 0:
                    self.dp[i][j] = 0
                elif self.weight[i-1] <= j: 
                    self.dp[i][j] = max(self.value[i-1] + self.dp[i-1][j-self.weight[i-1]], self.dp[i-1][j])
                else:
                    self.dp[i][j] = self.dp[i-1][j]

weight = [1,3,4,5]
value = [1,4,5,7]
capacity = 7

obj = video_5(weight, capacity, value)
obj._get_highest_profit()

