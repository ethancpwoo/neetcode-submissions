class Solution:
    def get_tuple(self, word):
        count = [0 for x in range(26)]
        for c in word:
            count[ord(c) - ord('a')] += 1
        return tuple(count)
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for word in strs:
            tup = self.get_tuple(word)
            if tup in ana_dict:
                ana_dict[tup].append(word)
            else:
                ana_dict[tup] = [word]
        return list(ana_dict.values())
        
