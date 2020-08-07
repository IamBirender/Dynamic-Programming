class video_3(object):
    def __init__(self, weight, value, capacity):
        self.weight = weight
        self.value = value
        self.capacity = capacity
        self.result = 0
    
    def _get_combinations(self):
        result =  self.__recursion(self.weight, self.value, self.capacity)
        return result

    def __recursion(self, weight, value, capacity):
        print(weight[1:], value[1:], capacity)
        if len(weight) == 0:
            return 0

        if weight[0] <= capacity:
            return max(value[0] + self.__recursion(weight[1:], value[1:], capacity - weight[0]), self.__recursion(weight[1:], value[1:], capacity))
        else:
            return self.__recursion(weight[1:], value[1:], capacity)
        
        

weight = [1,3,4,5]
value = [1,4,5,7]
capacity = 7

obj = video_3(weight, value, capacity)
print(obj._get_combinations())