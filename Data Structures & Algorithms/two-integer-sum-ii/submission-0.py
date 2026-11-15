class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # they are increasing, so once the sum increases past target, then change left pointer. 
        l, r = 0, len(numbers) - 1
        while l < r:
            n_sum = numbers[l] + numbers[r]
            if n_sum == target:
                return [l+1, r+1]
            if n_sum > target:
                r -= 1
            if n_sum < target:
                l += 1