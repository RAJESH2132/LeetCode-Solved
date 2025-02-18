class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, cap):
        self.capacity = cap
        self.cache = {}  # Dictionary to store key -> Node
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: Node):
        """Adds a node to the tail (most recently used position)."""
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def _remove(self, node: Node):
        """Removes a node from the doubly linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key):
        """Returns value if key exists, else -1."""
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)  # Move to most recently used
        self._add(node)
        return node.value

    def put(self, key, value):
        """Inserts or updates key-value pair. Removes LRU if full."""
        if self.capacity == 0:
            return  # If cache size is 0, do nothing

        if key in self.cache:
            node = self.cache[key]
            node.value = value  # Update existing node's value
            self._remove(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
        
        self._add(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next  # Least recently used node
            self._remove(lru)
            del self.cache[lru.key]

    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)