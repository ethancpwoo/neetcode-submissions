import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        top_k = [] 
        for num in nums:
            if num not in m:
                m[num] = 1
            else: 
                m[num] += 1
        for key, val in m.items():
            pair = (val, key) 
            heapq.heappush_max(top_k, pair)
        return [heapq.heappop_max(top_k)[1] for i in range(k)]