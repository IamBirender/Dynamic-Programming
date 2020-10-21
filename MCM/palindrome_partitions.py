from time import perf_counter 

class palindrome_partition(object):
    def __init__(self, string):
        self.string = string
        self.l = len(string)
        self.memo = [[-1 for i in range(self.l)] for j in range(self.l)]
    
    def solve(self):
        a = perf_counter()
        print(self._recursive_solution(0, len(self.string)))
        b = perf_counter()
        print(self._memo_solution(0, self.l))
        c = perf_counter()
        print("without_memo = ", b-a, " with_memo = ", c-b)

    def _recursive_solution(self, i, j):

        if self._is_palindrome(i, j) or i >= j:
            return 0
        answer = float("inf")
        for k in range(i+1, j):
            temp = self._recursive_solution(i, k) + 1 + self._recursive_solution(k, j)
            answer = min(temp, answer)
        return answer
    
    def _memo_solution(self, i, j):
        
        if self._is_palindrome(i, j) or i >= j:
            return 0
        
        answer = float("inf")
        
        for k in range(i+1, j):
            if self.memo[i-1][j-1] != -1:
                return self.memo[i-1][j-1]
            temp = self._recursive_solution(i, k) + 1 + self._recursive_solution(k, j)
            answer = min(temp, answer)
        self.memo[i-1][j-1] =answer
        return self.memo[i-1][j-1]
            
            
    def _is_palindrome(self, i, j):
        if self.string[i:j] == self.string[i:j][::-1]:
            return True
        else:
            return False
        
        

name = "b"
obj = palindrome_partition(name)
obj.solve()
