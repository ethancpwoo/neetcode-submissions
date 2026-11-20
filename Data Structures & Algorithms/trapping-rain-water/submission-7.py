class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        volume = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(height[l], l_max)
                volume += l_max - height[l]
            else:
                r -= 1
                r_max = max(height[r], r_max)
                volume += r_max - height[r]
        return volume



        # prefix_max, suffix_max = [], [0 for x in range(len(height))]
        # max_pre = 0
        # max_suf = 0
        # for i in range(len(height)):
        #     max_pre = max(max_pre, height[i])
        #     max_suf = max(max_suf, height[len(height)-1-i])
        #     prefix_max.append(max_pre)
        #     suffix_max[len(height)-1-i] = max_suf
        # volume = 0 
        # for i in range(len(height)):
        #     volume += min(prefix_max[i], suffix_max[i]) - height[i]
        # return volume
        

       # # This would work, but would not be O(n) and 
       # first, second = 0, 1
       # volume = 0
       # 
       # while first < len(height)-1 and second < len(height)-1:
       #     diff = height[first] - height[second]
       #     if diff > 0:
       #         sub = 0
       #         while height[second] < height[first] and second < len(height)-1:
       #             sub += height[second]
       #             second += 1
#
       #             
       #         volume += diff 
       #         second += 1
       #     else:
       #         first = second
       #         second += 1
       # 
       # return volume
         
                
            