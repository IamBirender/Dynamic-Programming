class solution(object):
    def __init__(self, str1):
        self.str1 = str1
        self.str2 = str1[::-1]
        self.len1 = self.len2 = len(str1)
        self.memo = [[0 for i in range(self.len2+1)] for j in range(self.len1+1)]
        self.dp = [[0 for i in range(self.len2+1)] for j in range(self.len1+1)]
        
    def _get_min_insertion(self):
        # print(self.len1 - self.__recursive_solution(self.len1, self.len2))
        # print(self.len1 - self.__rec_with_memo(self.len1, self.len2))
        print(self.len1 - self.__top_down_approach())
    
    def __recursive_solution(self, i, j):
        if i == 0 or j == 0:
            return 0
        
        if self.str1[i-1] == self.str2[j-1]:
            return 1 + self.__recursive_solution(i-1, j-1)
        else:
            return max(self.__recursive_solution(i-1,j), self.__recursive_solution(i,j-1))
    
    def __rec_with_memo(self, i, j):
        if i == 0 or j == 0:
            return 0

        if self.memo[i][j]:
            return self.memo[i][j]
        
        if self.str1[i-1] == self.str2[j-1]:
            self.memo[i][j] = 1 + self.__recursive_solution(i-1, j-1)
        else:
            self.memo[i][j] = max(self.__rec_with_memo(i-1, j), self.__rec_with_memo(i, j-1))
        return self.memo[i][j]

    def __top_down_approach(self):
        for i in range(self.len1+1):
            for j in range(self.len2 +1):
                if i == 0 or j == 0:
                    self.dp[i][j] = 0
                elif self.str1[i-1] == self.str2[j-1]:
                    self.dp[i][j] = 1 + self.dp[i-1][j-1]
                else:
                    self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1])            
        return self.dp[-1][-1]

str1 = "aekbcbda"
    #    "adbcbea"

obj = solution(str1)
obj._get_min_insertion()

