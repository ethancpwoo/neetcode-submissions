class Node:
    def __init__(self, key, val, prev, next):
        self.val = val 
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur = 0 
        self.head = None
        self.last = None
        self.node_cache = {}

    def get(self, key: int) -> int:
        if key in self.node_cache:
            temp_next = self.node_cache[key].next
            temp_prev = self.node_cache[key].prev
            if temp_next: 
                temp_next.prev = temp_prev
            else: # it must be the last node, so dont touch anything
                return self.last.val

            if temp_prev:
                temp_prev.next = temp_next
            else: # head node, adjust accordingly
                self.head = self.head.next
                self.head.prev = None

            self.last.next = self.node_cache[key]
            self.node_cache[key].prev = self.last
            self.node_cache[key].next = None
            self.last = self.node_cache[key]
            return self.last.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.head is None: # Nothing in cache
            self.node_cache[key] = Node(key, value, None, None)
            self.head = self.node_cache[key]
            self.last = self.node_cache[key]
            self.cur += 1

        elif key not in self.node_cache and self.cur < self.capacity: 
            self.node_cache[key] = Node(key, value, self.last, None)
            self.last.next = self.node_cache[key]
            self.last = self.node_cache[key]
            self.cur += 1

        elif key in self.node_cache: #in cache, update
            temp_next = self.node_cache[key].next
            temp_prev = self.node_cache[key].prev

            if temp_next:
                temp_next.prev = temp_prev
            else: # no next means its the tail, no need to move
                self.node_cache[key].val = value
                return

            if temp_prev:
                temp_prev.next = temp_next
            else: # means that its the head
                self.head = self.head.next
                self.head.prev = None
                
            self.last.next = self.node_cache[key]
            self.node_cache[key].prev = self.last
            self.node_cache[key].next = None
            self.node_cache[key].val = value
            self.last = self.node_cache[key]
        else: # no capacity
            old_head = self.head
            self.node_cache.pop(old_head.key)

            if self.head == self.last:
                self.head = None
                self.last = None
            else:
                self.head = old_head.next
                self.head.prev = None
        
            new_node = Node(key, value, self.last, None)
            self.node_cache[key] = new_node
        
            if self.last is None:
                self.head = new_node
                self.last = new_node
            else:
                self.last.next = new_node
                self.last = new_node