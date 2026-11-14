class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {} 
        for letter in s:
            if letter in check:
                check[letter] += 1
            else:   
                check[letter] = 1

        verify = {} 
        for letter in t:
            if letter in verify:
                verify[letter] += 1
            else:   
                verify[letter] = 1
        
        if verify != check:
            return False
        #for key in verify:
        #    if key not in check:
        #        return False
        #    if verify[key] != check[key]:
        #        return False
        return True