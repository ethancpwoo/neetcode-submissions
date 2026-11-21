class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ttr_map = {position[i]: (target-position[i])/speed[i] for i in range(len(position))}
        position = sorted(position)
        s = []
        for pos in position:
            ttr = ttr_map[pos]
            while len(s) and ttr >= s[-1]:
                s.pop()
            s.append(ttr)
        return len(s)
                