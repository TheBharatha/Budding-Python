class LRUCache:

    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity
        self.rank = 0
        

    def get(self, key):
        try:
            return(list(self.cache.values())[list(self.cache.keys()).index(key)])
        except:
            return(-1)
        
    def put(self, key, value):
        if len(self.cache) < self.capacity:
            self.cache[key] = [10, value+10]
            print(min(list(self.cache.values())[0]))
        self.cache[key] = [2, value]
        print('Out of condition ',min(list(self.cache.values())[0]))

if __name__ == "__main__":
    obj = LRUCache(3)
    for i in range(3):
        obj.put(i,i+1)
    for i in range(3):
        param_1 = obj.get(i)
        print(param_1)

'''
cahce = dict()
cahce[0] = [1,0]
cahce[1] = [2,5]
print(cahce)
list(cahce.values())[list(cahce.keys()).index(1)][1] = 3
print(len(cahce))
#print(list(cahce.values())[list(cahce.keys()).index(1)][1])
'''