class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_min = prices[0]
        max_prof = 0
        for idx in range(1, len(prices)):
            prof = (prices[idx] - b_min)
            max_prof = max(prof, max_prof)
            b_min = min(b_min, prices[idx])
        return max_prof