class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # immediately i think of hashmap and just check the counts
        # If they want o(1) space, it works since we can have dict
        # of all characters
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        for char in s1:
            s1_count[ord(char)] += 1
        
        l, r = 0, 0
        while (r < len(s2)):
            s2_count[ord(s2[r])] += 1
            while s2_count[ord(s2[r])] > s1_count[ord(s2[r])]: 
                s2_count[ord(s2[l])] -= 1
                l += 1
            if s1_count == s2_count:
                return True
            r += 1
        return False