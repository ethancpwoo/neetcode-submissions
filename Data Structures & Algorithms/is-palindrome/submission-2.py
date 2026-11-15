class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = {}
        start_letter = ord('a')
        end_letter = ord('z')
        start_num =  ord('0')
        end_num = ord('9') 
        for i in range(start_letter, end_letter):
            valid[chr(i)] = 1
        for i in range(9):
            valid[chr(i)] = 1
        
        s = ''.join(s.lower().split(' ')) 
        new_s = '' 
        for c in s:
            if c.isalnum():
                new_s += c

        l, r = 0, len(new_s)-1
        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l, r = l+1, r-1

        return True