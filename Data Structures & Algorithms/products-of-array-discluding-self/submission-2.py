class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        res = []
        for idx, num in enumerate(nums):
            res.append(pro)
            pro *= num
        pre = 1 
        for idx in range(len(nums)-2, -1, -1):
            pre *= nums[idx+1]
            res[idx] *= pre
        return res
        