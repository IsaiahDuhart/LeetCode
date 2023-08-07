from ast import List

#A) Loop through list, checking if any elements after curr index are anagrams, has O(n!) loops :(
#B) Loop through list, create dictionary with keys of dictionaries for frequency of letters and values of indices in original list O(n) loops
#   If not big_dict has key little dict: Add key and val
#   else: add index to vals
#   Loop through vals of big_dict and create little list of vals and put it in big list of all word O(n) loops
# Yay, linear solution!!!!


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = [[]]
        little_dict = {}
        big_dict = {}
        for x in strs:
            little_dict = self.findFreq(x)
            if not little_dict in big_dict.values():
                big_dict[len(big_dict)] = little_dict
            if little_dict in big_dict.values():
                ret[list(big_dict.values()).index(little_dict)].append(x)
        return ret
    
    def findFreq(self, s: str) -> dict:
        dict = {}
        for x in s:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        return dict