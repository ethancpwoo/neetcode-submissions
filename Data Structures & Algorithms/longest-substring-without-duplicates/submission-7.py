class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: 
            return 0

        max_len = 1
        cur_len = 1
        l, r = 0, 1
        appeared = {s[l]: 0}

        while r < len(s):
            while s[r] in appeared:
                appeared.pop(s[l])
                l += 1
                cur_len -= 1
            appeared[s[r]] = r
            r+=1
            cur_len += 1
            max_len = max(cur_len, max_len)
        
        return max_len
            
            
