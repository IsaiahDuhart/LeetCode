from ast import List

#A) Loop through list, checking if any elements after curr index are anagrams, has O(n!) loops :(
#B) Loop through list, create dictionary with keys of dictionaries for frequency of letters and values of indices in original list O(n) loops
#   If not big_dict has key little dict: Add key and val
#   else: add index to vals
#   Loop through vals of big_dict and create little list of vals and put it in big list of all word O(n) loops
#   Yay, linear solution!!!!
#   No :( this doesn't work
#C) Loop through list, alphabitizes words ("eats" -> "aest"), -- hopefully O(n) soln
#   Now sort list in alphabetical order -- O(nlogn)
#   Now anagram groups are adjacent, we just need to find the between groups where words sorted aplphabetically are not equal -- O(n) soln
#   O(n + nlogn + n) = O(nlogn)!
#   Uh oh, I won't know which words the rearranged words are supposed to represent
#D) Use dictionary to store sorted words, with rearranged words as the keys and list of original words as the value -- O(n) soln (we just have to loop through list once then return values of dictionary)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphaStrs = {}
        for x in strs:
            alpha = "".join(sorted(x))
            if alpha in alphaStrs:
                alphaStrs[alpha].append(x)
            else:
                alphaStrs[alpha] = [x]
        return list(alphaStrs.values())
    

