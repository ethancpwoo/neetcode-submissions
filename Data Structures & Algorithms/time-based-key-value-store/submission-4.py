class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ls = self.time_map[key]
        if len(ls) == 0:
            return ""
        l, r = 0, len(ls)-1
        while l+1 < r:
            m = (l+r)//2
            if m == l:
                return ls[m][1]
            if ls[m][0] == timestamp:
                return ls[m][1]
            elif ls[m][0] < timestamp:
                l = m
            elif ls[m][0] > timestamp:
                r = m - 1
        if ls[r][0] <= timestamp:
            return ls[r][1]
        if ls[l][0] <= timestamp:
            return ls[l][1]
        return ""
        