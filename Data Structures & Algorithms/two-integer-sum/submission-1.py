class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for idx, num in enumerate(nums):
            m[num] = idx
        for idx, num in enumerate(nums):
            res = target - num
            if (res in m):
                if idx != m[res]:
                    return [idx, m[res]] 