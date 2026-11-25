# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        res = head 
        carry = 0
        while l1 or l2 or carry == 1:
            if l1 and l2:
                res_sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif not l1 and l2:
                res_sum = l2.val + carry
                l2 = l2.next
            elif not l2 and l1:
                res_sum = l1.val + carry
                l1 = l1.next
            else:
                res_sum = carry
                
            if res_sum >= 10:
                carry = 1
                res_sum = res_sum % 10
            else:
                carry = 0
            res.val = res_sum
            if l1 or l2 or carry == 1:
                res.next = ListNode()
                res = res.next
        return head