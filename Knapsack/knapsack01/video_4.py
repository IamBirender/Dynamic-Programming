class video_3(object):
    def __init__(self, weight, value, capacity):
        self.weight = weight
        self.value = value
        self.capacity = capacity
        self.N = len(weight)
        self.result = 0
        self.dp = [[0 for i in range(self.capacity+1)] for j in range(self.N+1)]
    
    def _get_combinations(self):
        result =  self.__recursion(self.weight, self.value, self.capacity, self.N)
        for d in self.dp:
            print(d)
        return result

    def __recursion(self, weight, value, capacity,N):

        if len(weight) == 0:
            return 0

        if self.dp[N][capacity]:
            return self.dp[N][capacity]

        if weight[N-1] <= capacity:
            self.dp[N][capacity] = max(value[N-1] + self.__recursion(weight[:-1], value[:-1], capacity - weight[N-1], N-1), self.__recursion(weight[:-1], value[:-1], capacity, N-1))
        else:
            self.dp[N][capacity] = self.__recursion(weight[:-1], value[:-1], capacity, N-1)
        
        return self.dp[N][capacity]
        
        

weight = [1,3,4,5,12,3,34,4,5]
value = [1,4,5,7,2,3,45,12,12]
capacity = 7

obj = video_3(weight, value, capacity)
print(obj._get_combinations())