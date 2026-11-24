# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, cur = None, None
        if list1 and list2: 
            if list1.val >= list2.val:
                head = list2
                list2 = list2.next
            else: 
                head = list1
                list1 = list1.next
            cur = head
        elif not list1:
            return list2
        else:
            return list1

        while cur:
            if not list1:
                cur.next = list2 
                break
            elif not list2:
                cur.next = list1
                break
            elif list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        return head
