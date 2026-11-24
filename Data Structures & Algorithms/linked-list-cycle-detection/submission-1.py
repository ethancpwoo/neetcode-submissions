# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        slow, fast = head.next, head.next.next
        while slow and fast and slow is not fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
        if (slow is fast) and slow and fast:
            return True
        return False