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

        half = int(len(new_s) / 2)
        parity = len(new_s) % 2
        i = 0
        stack = []
        print(new_s)
        while i < half:
            stack.append(new_s[i])
            i += 1
        print(stack)
        i = half + parity 
        while i < len(new_s):
            if stack.pop() != new_s[i]:
                return False 
            i+=1 

        return True