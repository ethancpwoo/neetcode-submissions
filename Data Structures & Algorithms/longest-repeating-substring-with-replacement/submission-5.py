class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 1
        l, r = 0,0 
        letter_map = {}
        most_frequent = 0 
        most_frequent_char = '' 
        while r < len(s):
            if s[r] in letter_map:
                letter_map[s[r]] += 1
            else:
                letter_map[s[r]] = 1

            if letter_map[s[r]] > most_frequent:
                most_frequent = letter_map[s[r]]

            while (r-l+1-most_frequent) > k: 
                letter_map[s[l]] -= 1
                if letter_map[s[l]] <= 0:
                    letter_map.pop(s[l])
                l+=1

            max_len = max(max_len, r-l+1)
            r += 1
        return max_len 
                


        