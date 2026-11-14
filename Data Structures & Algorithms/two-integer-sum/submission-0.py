class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for idx, num in enumerate(nums):
            m[num] = idx
        for idx, num in enumerate(nums):
            res = target - num
            if (res in m):
                if idx != m[res]:
                    i = max(idx, m[res])
                    j = min(idx, m[res])
                    return [j, i] 