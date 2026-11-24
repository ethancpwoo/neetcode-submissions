# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # After drawing out a few examples
        # Can see that indexes new transformed locations are index times 2. 
        # We can alternate, lets get a pointer 

        # find length
        cur = head
        length = 0
        while cur: 
            length += 1
            cur = cur.next
        mid = (length+1)//2
        print(mid)

        cur = head
        counter = 0
        while counter < mid-1:
            counter += 1
            cur = cur.next
        temp = cur.next
        cur.next = None
        cur = temp
        
        # reverse from cur:
        prev = None
        rev = cur
        while rev:
            temp = rev.next 
            rev.next = prev
            prev = rev
            rev = temp
        # prev is now the end with the rest of the list reversed.

        # build sorted
        end = prev
        cur = head
        while end: 
            left = cur.next
            right = end.next
            end.next = left
            cur.next = end
            cur = left
            end = right