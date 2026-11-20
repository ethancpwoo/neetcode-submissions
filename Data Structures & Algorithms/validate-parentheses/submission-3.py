class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1: 
            return False

        open_stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                open_stack.append(s[i])
            else:
                if open_stack:
                    open_pop = open_stack.pop()
                    if open_pop == '(' and s[i] != ')':
                        return False
                    elif open_pop == '{' and s[i] != '}':
                        return False
                    elif open_pop == '[' and s[i] != ']':
                        return False
                else: 
                    return False
        if open_stack:
            return False

        return True