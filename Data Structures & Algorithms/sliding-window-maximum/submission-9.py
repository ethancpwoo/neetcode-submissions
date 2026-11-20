class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # my mind goes to just using that window, sorting inside of that subarray and getting the max
        # is there an optimization? 
        # once we get the max of the initial one, if the num removed is less than the max, and the next one is less than it, then the max remains. 
        # if the max gets removed and the next one is not bigger, then you have to resort and get the new max
        # ls = []
        # for i in range(len(nums)-k+1): 
        #     sub = sorted(nums[i:i+k])
        #     ls.append(sub[-1])
        # return ls
        # it works but too slow. 
        # l, r = 0, 0 
        # ls = []
        # cur_max = nums[0]
        # while r < len(nums):
        #     cur_max = max(cur_max, nums[r])
        #     if r-l+1 == k:
        #         ls.append(cur_max)
        #         l += 1
        #         r = l
        #         if l < len(nums):
        #             cur_max = nums[l]
        #     else:
        #         r += 1
        # return ls
        # This is also too inefficient
        
        # So after giving my prev attempts to a chat bot, try to maybe judge if a new element that enters my window could be a candidate for a maximum? 
        from collections import deque 

        l, r = 0, 0
        cans = deque([])
        ls = []

        while r < len(nums):
            while cans and nums[r] >= nums[cans[-1]]:
                cans.pop()
            cans.append(r)
            if r-l+1 == k:
                ls.append(nums[cans[0]])
                if l == cans[0]:
                    cans.popleft()
                l += 1
            r += 1
        return ls
        