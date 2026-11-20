class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        prefix_max, suffix_max = [], [0 for x in range(len(height))]
        max_pre = 0
        max_suf = 0
        for i in range(len(height)):
            max_pre = max(max_pre, height[i])
            prefix_max.append(max_pre)
        for i in range(len(height)-1, -1, -1):
            max_suf = max(max_suf, height[i])
            suffix_max[i] = max_suf
        volume = 0 
        for i in range(len(height)):
            volume += min(prefix_max[i], suffix_max[i]) - height[i]
        return volume
        

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
         
                
            