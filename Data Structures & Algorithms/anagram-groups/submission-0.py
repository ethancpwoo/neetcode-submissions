class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in ana_dict:
                ana_dict[sorted_word].append(word)
            else:
                ana_dict[sorted_word] = [word]

        ls = []
        for key in ana_dict:
            ls.append(ana_dict[key])
        return ls
        
