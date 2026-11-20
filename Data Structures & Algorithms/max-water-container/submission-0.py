class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        dist = len(heights)
        max_volume = 0

        while l < r:
            lim = min(heights[l], heights[r])
            dist = r - l
            volume = lim * dist
            max_volume = max(volume, max_volume)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                l += 1
        return max_volume

