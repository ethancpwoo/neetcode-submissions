class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while s and temperatures[s[-1]] < temp:
                i = s.pop()
                res[i] = idx - i
            s.append(idx)
        return res