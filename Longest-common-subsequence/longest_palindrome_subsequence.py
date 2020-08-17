class solution(object):
    def __init__(self, str1):
        self.str1 = str1
        self.str2 = str1[::-1]
        self.len1 = len(self.str1)
        self.len2 = len(self.str2)
        self.res = ""
    
    def _get_longest_panlindrome(self):
        self.__recursive_solution(self.len1, self.len2, "")
        print(self.res)
    
    def __recursive_solution(self, i, j, palin_str):
        if i == 0 or j == 0:
            if palin_str == palin_str[::-1] and len(self.res) < len(palin_str):
                self.res = palin_str
            return 
        
        if self.str1[i-1] == self.str2[j-1]:
            self.__recursive_solution(i-1, j-1, self.str1[i-1]+palin_str)
        else:
            self.__recursive_solution(i-1, j, palin_str)
            self.__recursive_solution(i, j-1, palin_str)

str1 = "agbcba"
str2 = "abcbga"
obj = solution(str1)
obj._get_longest_panlindrome()
