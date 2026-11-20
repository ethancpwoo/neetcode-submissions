class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_min = prices[0]
        max_prof = 0
        for idx in range(len(prices)-1):
            prof = (prices[idx+1] - b_min)
            max_prof = max(prof, max_prof)
            b_min = min(b_min, prices[idx+1])
        return max_prof