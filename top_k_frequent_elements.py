from ast import List
import sys

#OMG I love dictoinaries <3
#A) loop through list, have numbers be keys with their frequencies as the keys - O(n)
#   loop through keys to find k biggest values - O(n)
#   O(n) soln
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        ret = []
        for x in nums:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        #I'm having trouble finding a good way to find the lowest frequency value when adding a new element to the list
        #Right now I have a lowestFreq array with two elements, one is the index of the array the number is in, and the second is that numbers frequency
        #The problem is that when I add a new element I'll have to go through the whole return array looking for the smallest frequency number again
        #This will add a k coefficient to my soln, but that doesn't really matter as it will get absorbed by n anyways.
        #Solution -- create a helper function that loops through the return array and returns the lowest frequency element's index and frequency
        lowestFreq = 0
        for key, value in dict.items():
            if not ret or len(ret) < k:
                ret.append(key)
                if value < dict[ret[lowestFreq]]:
                    lowestFreq = len(ret) - 1
            elif value > dict[ret[lowestFreq]]:
                del ret[lowestFreq]
                ret.insert(lowestFreq, key)
                for idx, x in enumerate(ret):
                    if dict[x] < dict[ret[lowestFreq]]:
                        lowestFreq = idx
        return ret

            



