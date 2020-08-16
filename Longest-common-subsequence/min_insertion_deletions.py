class solution(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.ll = len(self.str1)
        self.l2 = len(self.str2)
        self.res = ""
        self.memo = [[0 for i in range(self.l2+1)] for j in range(self.ll+1)] 
        self.dp = [[0 for i in range(self.l2+1)] for j in range( self.ll +1)]
    
    def _get_operations(self):
#         print(self.__recursive_approach(self.ll, self.l2))
#         print(self.__rec_with_memo( self.ll, self.l2))
#         for i in self.memo:
#             print(i)
        self.__top_down()
    
    def __recursive_approach(self, i, j):
        if i == 0 or j == 0:
            if i:
                return i
            else:
                return j
        
        if self.str1[i-1] == self.str2[j-1]:
            return self.__recursive_approach(i-1, j-1)
        else:
            return 1 + min(self.__recursive_approach(i-1, j), self.__recursive_approach(i, j-1))
        
    def __rec_with_memo(self, i, j):
        if i == 0 or j == 0:
            if i:
                self.memo[i][j] = i
                return i
            else:
                self.memo[i][j] = j
                return j
        
        if self.memo[i][j] != 0:
            return self.memo[i][j]
        
        if self.str1[i-1] == self.str2[j-1]:
            self.memo[i][j] = self.__rec_with_memo(i-1, j-1)
            
        else:
            self.memo[i][j] = 1 + min(self.__rec_with_memo(i-1, j), self.__rec_with_memo(i, j-1))
        return self.memo[i][j]
    
    def __top_down(self):
        for i in range(self.ll+1):
            for j in range(self.l2+1):
                if i == 0:
                    self.dp[i][j] = j
                elif j == 0:
                    self.dp[i][j] = i
                
                elif self.str1[i-1] == self.str2[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1]
                else:
                    self.dp[i][j] = 1 + min(self.dp[i-1][j], self.dp[i][j-1]) 
                    
        print("     ","  ".join(list(self.str2)))
        for i, l in enumerate(self.dp):
            
            if i:
                print(self.str1[i-1],l)
            else:
                print(" ", l)
        
        return self.dp[-1][-1]
    

str1 = "heapock"
str2 = "peacock"

obj = solution(str1, str2)
obj._get_operations()

