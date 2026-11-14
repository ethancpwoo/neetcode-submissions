import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num not in m:
                m[num] = 1
            else: 
                m[num] += 1
        for key, val in m.items():
            freq[val].append(key)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
