class solution(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.len1 = len(str1)
        self.len2 = len(str2)
        self.res = float("-inf")
        self.memo = [[-1 for i in range(self.len2+1)] for j in range(self.len1+1)]
        self.dp = [[-1 for i in range(self.len2+1)] for j in range(self.len1+1)]
    
    def get_longest_substring(self):
        self.__hypothesis(self.len1, self.len2,0)
        print(self.res)
        
        self.__rec_with_memo(self.len1, self.len2,0)
        print(self.res)
        print(self.__top_down())
    
    def __hypothesis(self, l1, l2, sublen):
        if l1 == 0 or l2 == 0:
            self.res = max(self.res, sublen)
            return 
        
        if self.str1[l1-1] == self.str2[l2-1]:
            self.__hypothesis(l1-1, l2-1, sublen+1)
        else:
            self.__hypothesis(l1-1, l2, 0)
            self.__hypothesis(l1, l2-1, 0)
        
        return sublen
    
    def __rec_with_memo(self, l1, l2, sublen):
        if l1 == 0 or l2 == 0:
            self.res = max(self.res, sublen)
            return 
        
        if self.memo[l1][l2]!=-1:
            return self.memo[l1][l2]
        
        if self.str1[l1-1] == self.str2[l2-1]:
            self.__hypothesis(l1-1, l2-1, sublen+1)
        else:
            self.__hypothesis(l1-1, l2, 0)
            self.__hypothesis(l1, l2-1, 0)
        
        return sublen
    
    def __top_down(self):
        for i in range(self.len1 + 1):
            for j in range(self.len2 + 1):
                if i == 0 or j == 0:
                    self.dp[i][j] = 0
                
                elif self.str1[i-1] == self.str2[j-1]:
                    self.dp[i][j] = 1 + self.dp[i-1][j-1]
                
                else:
                    self.dp[i][j] = 0
        
        for row in self.dp:
            self.res = max(self.res, max(row))
        return self.res

s1 = "abcdgh"
s2 = "abcdfhr"        
obj = solution(s1, s2)
obj.get_longest_substring()
