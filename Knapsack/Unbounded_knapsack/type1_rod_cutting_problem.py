class solution(object):
    def __init__(self, length, price, N):
        self.subparts = length
        self.price = price
        self.length = N
        self.subpart_types = len(length)
        self.max_profit = float("-inf")
        self.memo = [[-1 for i in range(N+1)] for j in range(N+1)]
        self.dp = [[0 for i in range(N+1)] for j in range(N+1)]
    
    def _get_maximum_profit(self):
        # return self.__recursion(self.subpart_types, self.length)
        # return self.__recursion_with_memo(self.subpart_types, self.length)
        self.__bottom_up()
        print(" ",self.price)
        print(" ", list(range(9)))
        for i, num in enumerate(self.dp):
            if not i:
                print("0", num)
            else:
                print(self.subparts[i-1], num)
    
    
    def __recursion(self, subpart_types, length):
        if length == 0 or subpart_types == 0:
            return 0

        if self.subparts[subpart_types-1] <= length:
            return max(self.price[subpart_types-1] + self.__recursion(subpart_types, length - self.subparts[subpart_types-1]), self.__recursion(subpart_types-1, length))
        else:
            return self.__recursion(subpart_types-1, length)
    
    def __recursion_with_memo(self, subpart_types, length):
        
        if length == 0 or subpart_types == 0:
            return 0
        
        if self.memo[subpart_types][length] != -1: 
            return self.memo[subpart_types][length]
        
        if self.subparts[subpart_types-1] <= length:
            self.memo[subpart_types][length] = max(self.price[subpart_types-1] + self.__recursion_with_memo(subpart_types, length - self.subparts[subpart_types-1]), self.__recursion_with_memo(subpart_types-1, length))
            return self.memo[subpart_types][length]
        else:
            self.memo[subpart_types][length] = self.__recursion_with_memo(subpart_types-1, length)
            return self.memo[subpart_types][length]
    
    def __bottom_up(self):
        for i in range(1,self.length+1):
            for j in range(1, self.length+1):
                if self.subparts[i-1] <= j:
                    self.dp[i][j] = max(self.price[i-1] + self.dp[i][j-self.subparts[i-1]], self.dp[i-1][j])
                else:
                    self.dp[i][j] = self.dp[i-1][j]
        return self.dp[-1][-1]
                
                        
length = [1,2 , 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
N = 8
obj = solution(length, price, N)
print(obj._get_maximum_profit())