class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check_map = {}
        for idx, num in enumerate(nums):
            check_map[num] = idx
        max_len = 0 
        cur_len = 0
        for idx, num in enumerate(nums):
            if (num-1) not in check_map:
                min_num = num
                while min_num in check_map:
                    cur_len += 1
                    min_num += 1
                max_len = max(max_len, cur_len)
                cur_len = 0
        return max_len
            

        
                