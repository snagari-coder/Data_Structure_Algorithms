from collections import OrderedDict

class LeaseRecentlyUsedCache:

    # initialising capacity
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    # we return the value of the key
    # that is queried in O(1) and return -1 if we
    # don't find the key in out dict / cache.
    # And also move the key to the end
    # to show that it was recently used.
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    # first, we add / update the key by conventional methods.
    # And also move the key to the end to show that it was recently used.
    # But here we will also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so we remove the first key (least recently used)

    def put(self,key,value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

# RUNNER
# initializing our cache with the capacity of 2
mycache = LeaseRecentlyUsedCache(2)
mycache.put(1,1)
print(mycache.cache)
mycache.put(2,2)
print(mycache.cache)
mycache.put(3,3)
print(mycache.cache)
print(mycache.get(1))
print(mycache.get(2))
print(mycache.cache)
