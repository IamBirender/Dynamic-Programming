class solution(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.len1 = len(str1)
        self.len2 = len(str2)
        self.memo = [[None for i in range(self.len2+1)] for j in range(self.len1+1)]
        self.dp = [[None for i in range(self.len2+1)] for j in range(self.len1+1)]
    
    def _does_substring_exist(self):
        # print(self.__recursive_solution( self.len1, self.len2))
        # print(self.__rec_with_memo(self.len1, self.len2))
        print(self.__top_down_approach())
    
    def __recursive_solution(self, i, j):
        if i == 0 or j == 0:
            if i:
                return False
            else:
                return True

        if self.str1[i-1] == self.str2[j-1] :
            return self.__recursive_solution(i-1, j-1)
        else:
            return self.__recursive_solution(i, j-1)
        
    def __rec_with_memo(self, i, j):
        if i == 0 or j == 0:
            return False if i else True

        if self.memo[i][j] != None:
            return self.memo[i][j]
            
        if self.str1[i-1] == self.str2[j-1]:
            self.memo[i][j] = self.__rec_with_memo(i-1, j-1)
        else:
            self.memo[i][j] = self.__rec_with_memo(i, j-1)
        return self.memo[i][j]
    
    def __top_down_approach(self):
        for i in range(self.len1+1):
            for j in range(self.len2 + 1):
                if i == 0:
                    self.dp[i][j] = True
                elif j == 0:
                    self.dp[i][j] = False
                elif self.str1[i-1] == self.str2[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1]
                else:
                    self.dp[i][j] = self.dp[i][j-1]
        return self.dp[-1][-1]
    
str1 = "AXY"
str2 = "ACXTY"
obj = solution(str1, str2)
obj._does_substring_exist()
