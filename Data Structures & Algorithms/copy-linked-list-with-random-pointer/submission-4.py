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

        # have singly linked his
        while cur:
            check_map[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        new_head = check_map[cur]
        new_cur = new_head

        while cur:
            new_cur.random = check_map.get(cur.random, None)
            new_cur.next = check_map.get(cur.next, None)
            cur = cur.next
            new_cur = new_cur.next

        return new_head
