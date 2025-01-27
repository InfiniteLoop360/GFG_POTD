from collections import OrderedDict

class LRUCache:
    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.cap = cap
        self.cache = OrderedDict()  # OrderedDict maintains the insertion/access order.

    # Function to return value corresponding to the key.
    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end to mark it as recently used.
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    # Function for storing key-value pair.
    def put(self, key, value):
        if key in self.cache:
            # Update the value and mark the key as recently used.
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.cap:
            # Remove the least recently used key (the first item in the OrderedDict).
            self.cache.popitem(last=False)
        # Add the new key-value pair to the cache.
        self.cache[key] = value
