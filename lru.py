""" LRU Cache implementation """


class Node:
    def __init__(self, value) -> None:
        super().__init__()
        self.next = None
        self.prev = None
        self.key = None
        self.value = value


class LRUCache(object):

    def __init__(self, capacity):
        super().__init__()
        self.max_capacity = capacity
        self.current_capacity = 0
        self.cache = dict()
        self.most_recent = None
        self.least_recent = None

    def set_most_recent(self, node):
        self.most_recent.next = node
        node.prev = self.most_recent
        node.next = None
        self.most_recent = node

    def update_recency(self, node):
        if self.most_recent == node:
            return
        elif self.least_recent == node:
            self.least_recent = node.next
            self.least_recent.prev = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        self.set_most_recent(node)

    def get(self, key):
        if not key:
            return -1
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update_recency(node)
        return node.value

    def set(self, key, value):
        if not key or not value:
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            return  # should this be promoted to most recent?
        if self.current_capacity >= self.max_capacity:
            # insert new node as most recent
            node = Node(value)
            node.key = key
            self.cache[key] = node
            node.prev = self.most_recent
            self.most_recent.next = node
            self.most_recent = node
            # remove least recent node
            self.cache.pop(self.least_recent.key)
            self.least_recent = self.least_recent.next
            self.least_recent.prev = None
        elif self.current_capacity == 0:
            node = Node(value)
            node.key = key
            self.cache[key] = node
            self.least_recent = node
            self.most_recent = node
            self.current_capacity += 1
        else:  # self.current_capacity < self.max_capacity and sel.current_capacity > 0
            node = Node(value)
            node.key = key
            self.cache[key] = node
            self.most_recent.next = node
            node.prev = self.most_recent
            self.most_recent = node
            self.current_capacity += 1


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values


# Test Case 1
for i in range(0, 1000):
    our_cache.set(i, i)

# Test Case 2
for i in range(999, 900, -1):
    our_cache.get(i)

# Test Case 3
our_cache.get(None)
our_cache.set(None, None)
