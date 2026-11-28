# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # I think of a sliding window solution, it goes forward k, reverses then goes again
        r = head
        l = head
        old_last = None
        while True: 
            count = 1 
            # get right pointer
            while r and count < k:
                count += 1
                r = r.next
            if r is None:
                break
            next_k = r.next
            new_tail = r
            new_front = l

            # r should be at kth element of group, l should be at start
            # reverse that part of the linked list
            prev = None
            while prev is not r:
                temp_next = l.next
                l.next = prev
                prev = l
                l = temp_next

            # fix list
            if old_last is None:
                head = new_tail
                old_last = new_front
            else:
                old_last.next = new_tail
                old_last = new_front
            l, r = next_k, next_k
        
        if old_last:
            old_last.next = l

        return head
        
            
        