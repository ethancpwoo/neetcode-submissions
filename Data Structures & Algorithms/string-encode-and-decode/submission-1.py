class Solution:
    def encode(self, strs: List[str]) -> str:
        send = ''
        for word in strs:
            send += str(len(word))
            send += '#'
            send += word
        return send
        
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            length = ''
            while s[j] != '#':
                length += s[j]
                j+=1
            length = int(length)
            x = j+length+1
            strs.append(s[j+1:x])
            i = x 
        return strs

             
