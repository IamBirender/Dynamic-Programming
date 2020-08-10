class solution(object):
    def __init__(self, coin_array, net):
        self.coin_array = coin_array
        self.net = net
        self.N = len(self.coin_array)
        self.min_coins = float("inf")
        self.memo = [[-1 for i in range(self.net)] for j in range(self.N)]
        
    def _get_minimum_number_coins(self):
#         self.__recursive_way(self.N, self.net, list())
#         print(self.min_coins)
        self.__rec_with_memo(self.N, self.net, list())

    def __recursive_way(self, N, net, coins):
        if N == 0 or net == 0:
            if net ==0:
                print(N, net, coins)
                self.min_coins = min(self.min_coins, len(coins))
            return 
        
        if self.coin_array[N-1] <= net:
            self.__recursive_way( N, net-self.coin_array[N-1], coins + [self.coin_array[N-1]])
            self.__recursive_way( N-1, net, coins)
        else:
            self.__recursive_way(N-1, net, coins)
    
    def __rec_with_memo(self, N, net, coins):
        if N == 0 or net == 0:
            if net ==0:
                print(N, net, coins)
                self.min_coins = min(self.min_coins, len(coins))
            return 
        
        if self.memo[N][net] != -1:
            return self.memo[N][net]
        
        if self.coin_array[N-1] <= net:
            self.memo[N][net] = self.__rec_with_memo( N, net-self.coin_array[N-1], coins + [self.coin_array[N-1]])
            self.__rec_with_memo( N-1, net, coins)
        else:
            self.__rec_with_memo(N-1, net, coins)
        
            

coin = [1,2,3]
total = 5
obj = solution(coin, total)
print(obj._get_minimum_number_coins())
