# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        out_head = None
        max_cur_val = float('-inf')
        num_end = 0
        nums = []
        heapq.heapify(nums)
        while num_end < len(lists):
            num_end = 0
            for idx, head in enumerate(lists):
                if lists[idx]:
                    heapq.heappush(nums, lists[idx].val)
                    lists[idx] = lists[idx].next
                else:
                    num_end += 1
        if nums:
            out_head = ListNode(heapq.heappop(nums))
            cur = out_head
        else: 
            return None
            
        while nums:
            cur.next = ListNode(heapq.heappop(nums))
            cur = cur.next
    
        return out_head

                