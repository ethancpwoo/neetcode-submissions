class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_check = {} 
        s_check = {} 
        best_l = 0
        best_r = -1 
        for char in t:
            s_check[char] = 0
            if char not in t_check:
                t_check[char] = 1
            else:
                t_check[char] += 1
        need = len(t_check.keys())
        l, r = 0, 0
        have = 0
        while r < len(s):
            if s[r] in t_check:
                s_check[s[r]] += 1
                if s_check[s[r]] == t_check[s[r]]:
                    have += 1
            while have == need:
                if s[l] in t_check:
                    s_check[s[l]] -= 1
                    if s_check[s[l]] < t_check[s[l]]:
                        have -= 1
                cur_diff = r-l+1 
                if best_r == -1 or best_r-best_l > r-l: 
                    best_l, best_r = l, r
                l += 1
            r += 1

        if best_r == -1: 
            return ""
        return s[best_l:best_r+1]