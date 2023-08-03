from ast import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic ={}
        for x in nums:
            if x in dic:
                return True
            else:
                dic[x] = x
                
        return False
