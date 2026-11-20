class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = {} 
        for fixed in range(1, len(nums)-1):
            l, r = 0, len(nums)-1
            while l < fixed and r > fixed:
                cur_sum = nums[l] + nums[r] + nums[fixed]
                if cur_sum == 0:
                    res[(nums[l], nums[fixed], nums[r])] = 1
                    prev_l = nums[l]
                    prev_r = nums[r] 
                    while l < fixed and prev_l == nums[l]: 
                        l +=1
                    while r > fixed and prev_r == nums[r]: 
                        r -= 1
                if cur_sum > 0:
                    r -= 1
                if cur_sum < 0:
                    l += 1
        res_ls = []
        for key in res.keys():
            res_ls.append([*key])
        return res_ls