class solution(object):
    def __init__(self, length, price, N):
        self.subparts = length
        self.price = price
        self.length = N
        self.subparts_types = len(length)
        self.max_profit = float("-inf")
    
    def _get_maximum_profit(self):
        return self.__hypothesis(self.subparts_types, self.length)
    
    def __hypothesis(subpart_types, length):
        #base condition
        if length == 0 or subpart_types == 0:
            return 0

        if self.subparts[subpart_types-1] <= length:
            return max(self.price[subpart_types-1] + self.__hypothesis(subpart_types, length - self.subpart_types[subpart_types-1]), self.__hypothesis(subpart_types-1, length))
        else:
            return self.__hypothesis(subpart_types-1, length)
        

length = list(range(1,9))
price = [1, 5, 8, 9, 10,17,17,20]
N = 8
obj = solution(length, price, N)
print(obj._get_maximum_profit())