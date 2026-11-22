class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r = 0, len(nums)-1
        # while l < r:
        #     mid = (l+r)//2
        #     if nums[l] < nums[r]:
        #         return nums[l]
        #     elif nums[mid] > nums[l] and nums[mid] > nums[r]:
        #         l = mid + 1 
        #     elif nums[mid] < nums[l] and nums[mid] < nums[r]:
        #         r = mid 
        #     elif mid == l:
        #         return nums[r]
        # return nums[r] 

        l, r = 0, len(nums)-1
        res = nums[0] 
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else: 
                r = m-1
        return res