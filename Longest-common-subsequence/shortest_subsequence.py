class solution(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.l1 = len(str1)
        self.l2 = len(str2)
        self.res = list()
        self.memo = [[0 for i in range(self.l2+1)] for j in range(self.l1+1)]
        self.dp = [[0 for i in range(self.l2+1)] for j in range(self.l1 + 1)]
    
    def _get_super_sequence(self):
#         self.__recursive_solution(self.l1, self.l2, "")
#         self.__rec_with_memo(self.l1, self.l2)
        self.__top_down_approach()
#         print(len(self.res), len(set(self.res)))
#         for st in sorted(self.res, key = lambda x: len(x)):
#             print(st)
#         print(self.__get_substring(self.l1, self.l2))
        self.memo = self.dp
        print(self.__get_substring(self.l1, self.l2))
#         for i in self.memo:
#             print(i)
    def __recursive_solution(self,i, j, substr):
        if i == 0 or j ==0:
            if j:
                substr = self.str2[:j] + substr
            elif i:
                substr = self.str1[:i] + substr
            
            self.res.append(substr)
            return 
        
        if self.str1[i-1] == self.str2[j-1]:
            self.__recursive_solution(i-1, j-1, self.str1[i-1]+substr)
        else:
            self.__recursive_solution(i-1, j,  self.str1[i-1]+substr)
            self.__recursive_solution(i, j-1,  self.str2[j-1]+substr)
        
    def __rec_with_memo(self,i, j):
        if i == 0 or j == 0:
            if i:
                self.memo[i][j] = i
            else:
                self.memo[i][j] = j
            return self.memo[i][j]
        
        if self.memo[i][j] != 0:
            return self.memo[i][j]
        
        if self.str1[i-1] == self.str2[j-1]:
            self.memo[i][j] = 1+self.__rec_with_memo(i-1, j-1)
            return self.memo[i][j]
        
        else:
            self.memo[i][j] = min(1+self.__rec_with_memo(i-1, j), 1+self.__rec_with_memo(i,j-1))
            return self.memo[i][j]
    
    def __get_substring(self, i, j):
        substr = ""
        while i > 0 and j > 0:
            print("befor ", i,j, substr )
            if self.str1[i-1] == self.str2[j-1]:
                substr = self.str1[i-1] + substr
                i -= 1
                j -= 1
            else:
                if self.memo[i-1][j] < self.memo[i][j-1]:
                    substr = self.str1[i-1] + substr
                    i -= 1
                else:
                    substr = self.str2[j-1] + substr
                    j -= 1
            print("after ",i, j, substr)
            
        if i:
            substr = self.str1[:i]+substr
        if j:
            substr = self.str2[:j]+substr
        return substr
    
    def __top_down_approach(self):
        for i in range(self.l1+1):
            for j in range(self.l2 + 1):
                if i == 0:
                    self.dp[i][j] = j
                elif j == 0:
                    self.dp[i][j] = i
                    
                elif self.str1[i-1] == self.str2[j-1]:
                    self.dp[i][j] = 1+ self.dp[i-1][j-1]
                else:
                    self.dp[i][j] = 1 + min(self.dp[i-1][j], self.dp[i][j-1])
        for i in self.dp:
            print(i)
        return self.dp[-1][-1]
    
    
str2 = "AGGTAB"
str1 = "GXTXAYB"
obj = solution(str1, str2)
obj._get_super_sequence()

        
