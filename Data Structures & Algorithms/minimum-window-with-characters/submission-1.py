class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_check = defaultdict(int)
        s_check = defaultdict(int) 
        best_sub = ''
        for char in t:
            t_check[ord(char)] += 1
        need = len(t_check.keys())
        l, r = 0, 0
        have = 0
        while r < len(s):
            if ord(s[r]) in t_check:
                s_check[ord(s[r])] += 1
                if s_check[ord(s[r])] == t_check[ord(s[r])]:
                    have += 1
            while have == need:
                if ord(s[l]) in t_check:
                    s_check[ord(s[l])] -= 1
                    if s_check[ord(s[l])] < t_check[ord(s[l])]:
                        have -= 1
                cur_sub = s[l:r+1]
                if best_sub == '':
                    best_sub = cur_sub
                elif len(cur_sub) < len(best_sub):
                    best_sub = cur_sub
                l += 1
            r += 1

        return best_sub