class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_map = {position[i]: speed[i] for i in range(len(position))}
        position = sorted(position)
        s = []
        for pos in position:
            ttr = (target - pos)/speed_map[pos]
            while len(s) and ttr >= s[-1]:
                s.pop()
            s.append(ttr)
        return len(s)
                