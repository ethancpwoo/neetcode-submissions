"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        cur = head
        check_map = {}
        new_head = Node(cur.val, None, None)
        new_cur = new_head

        # have singly linked his
        while cur:
            check_map[cur] = new_cur 
            if cur.next:
                new_cur.next = Node(cur.next.val, None, None)
            else:
                new_cur.next = None
            cur = cur.next 
            new_cur = new_cur.next
            
        cur = head
        new_cur = new_head

        while cur:
            if cur.random is None:
                new_cur.random = None
            else:
                new_cur.random = check_map[cur.random]
            cur = cur.next
            new_cur= new_cur.next

        return new_head
