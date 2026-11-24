# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of ls
        size = 0
        cur = head
        while cur:  
            size += 1
            cur = cur.next
        
        # removal idx
        rm_idx = size-n

        cur = head
        prev = None
        counter = 0
        while counter < rm_idx: 
            counter += 1
            prev = cur
            cur = cur.next
        
        # remove it
        # account for head case:
        if cur is head:
            head = head.next
            return head
        
        if cur:
            prev.next = cur.next
        else:
            prev.next = None

        return head 
        