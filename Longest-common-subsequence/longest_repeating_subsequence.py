class solution(object):
    def __init__(self, str1):
        self.str2 = self.str1 = str1
        self.len2 = self.len1 = len(str1)
        self.result = ""
        self.memo = [[0 for i in range(self.len2+1)] for j in range(self.len1+1)]
    
    def _get_subsequence(self):
        # self.__recursive_solution(self.len1, self.len2, "")
        # print(self.result)
        
        print(self.__rec_with_memo(self.len1, self.len2, ""))
        for i in self.memo:
            print(i)
    
    def __recursive_solution(self, i, j, substr):
        
        if i == 0 or j == 0:
            if len(self.result) < len(substr):
                self.result = substr
            return 
        
        if self.str1[i-1] == self.str2[j-1] and i != j:
            # print(self.str1[:i], self.str2[:j], substr)
            self.__recursive_solution(i-1, j-1, self.str1[i-1] + substr)
        else:
            self.__recursive_solution(i-1, j, substr)
            self.__recursive_solution(i, j-1, substr)
    
    def __rec_with_memo(self, i, j, substr):
        print(self.str1[:i+1], self.str2[:j+1], substr)
        if i == 0 or j == 0:
            return substr
        
        if self.memo[i][j] != 0:
            return self.memo[i][j] 
        
        print(i, j, substr)
        if self.str1[i-1] == self.str2[j-1] and i != j:
            self.memo[i][j] = self.__rec_with_memo(i-1, j-1, self.str1[i-1] + substr)
        else:
            a = self.__rec_with_memo(i-1, j, substr)
            b = self.__rec_with_memo(i, j-1, substr)
            self.memo[i][j] = a if len(a) > len(b) else b
            
        return self.memo[i][j] 

str1 = "AABBCCDD"
obj = solution(str1)
obj._get_subsequence()