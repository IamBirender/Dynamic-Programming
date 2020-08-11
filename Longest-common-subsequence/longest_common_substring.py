
class Solution(object):
    def __init__(self, str1, str2):
        self.str1 = str1 
        self.str2 = str2
        self.l1 = len(str1)
        self.l2 = len(str2)
        self.memo = [[-1 for i in range(self.l1 + 2)] for j in range(self.l2 + 2)]
    
    def _get_LCS(self):
#         return self.__recursive_solution(self.l1, self.l2)
        self.__recursion_with_memo(self.l1, self.l2)
        for i in self.memo:
            print(i)
    
    def __recursive_solution(self, p1, p2):
        if p1 == 0 or p2 == 0:
            return 0
        
        if self.str1[p1-1] == self.str2[p2-1]:
            return 1 + self.__recursive_solution(p1-1, p2-1)
        else:
            return max(self.__recursive_solution(p1-1, p2) ,self.__recursive_solution(p1, p2-1))
    
    def __recursion_with_memo(self, p1, p2):
        if p1 == -1 or p2 == -1:
            return 0
        
        if self.memo[p1][p2] != -1:
            return self.memo[p1][p2]
        
        if self.str1[p1-1] == self.str2[p2-1]:
            self.memo[p1][p2] = 1 + self.__recursion_with_memo(p1-1, p2-1)
        else:
            self.memo[p1][p2] = max(self.__recursion_with_memo(p1-1, p2) ,self.__recursion_with_memo(p1, p2-1))
        return self.memo[p1][p2]
        
        
s1 = "abcdgh"
s2 = "abedfhr"
obj = Solution(s1, s2)
obj._get_LCS()
