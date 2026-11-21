class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       # wtf is this question
       # my first thought was a dynamic programming approach but the topic says stack
        # okay so key intuition is that once we see something less, then it doesnt matter what the original value was, they all become that less value because it doesnt make a difference to the total.
        # the issue becomes on the forward pass. 
        # maybe 2 passes? 
        # There is also if I iterate through the array again once i reach a max
        # s = []
        # max_h = 0
        # for idx, h in enumerate(heights):
        #     count = 0 
        #     max_h = max(max_h, h)
        #     if s and h >= s[-1]:
        #         s.append(h)
        #         l = len(s)-1
        #         while l > -1:
        #             max_h = max(max_h, s[l] * (len(s)-l))
        #             l -= 1
        #     elif s and h < s[-1]:
        #         while s and h <= s[-1]:
        #             s.pop()
        #             count += 1
        #         for i in range(count): 
        #             s.append(h)
        #         max_h = max(max_h, h * (count+1))
        #         s.append(h)
        #     else:
        #         s.append(h)
        # 
        # return max_h
        # this solution was too slow. There can be some optimization. 
            
            
        s = []
        max_area = 0
        heights.append(0)
        for idx, h in enumerate(heights):
            while s and h < heights[s[-1]]:
                r = s.pop()
                if s:
                    l = s[-1]
                else:
                    l = -1
                max_area = max(max_area, heights[r] * (idx-l-1))
            s.append(idx)
        return max_area
