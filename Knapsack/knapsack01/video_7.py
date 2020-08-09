class video_7(object):
    def __init__(self, arr, sum):
        self.array = arr
        self.sum = sum
        self.dp = [False for i in range()]
    
    def _subset_exist(self):
        return self.__hypothesis(self.array, self.sum)
    
    def __hypothesis(self, array, sum):
        #
        if sum == 0:
            return True
        

        if len(array) and array[-1] <= sum:
            return self.__hypothesis(array[:-1], sum - array[-1]) or self.__hypothesis(array[:-1], sum)
        elif len(array) and array[-1] > sum:
            return self.__hypothesis(array[:-1], sum)
        else:
            return False 

array = [2,3,7,8,10]
sum = 2
obj = video_7(array, sum)
print(obj._subset_exist())
