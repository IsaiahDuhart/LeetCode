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
    
#This is the efficient solution, it's 4 lines LOL

# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
#         # O(1) time 
#         if k == len(nums):
#             return nums
        
#         # 1. build hash map : character and how often it appears
#         # O(N) time
#         count = Counter(nums)   
#         # 2-3. build heap of top k frequent elements and
#         # convert it into an output array
#         # O(N log k) time
#         return heapq.nlargest(k, count.keys(), key=count.get) 

# Takeaways:
    #1) I've used this structure: 
        # dict = {}
        # for x in nums:
        #             if x in dict:
        #                 dict[x] += 1
        #             else:
        #                 dict[x] = 1
    # a lot to find the frequency of elements in a list, instead I can use the counter class and do this instead:
        #count = Counter(arr)
    #2) I learned about heaps from the solution article, heaps are the binary heaps we learned about in 3114, and I can use heapq in python to easily sort a frequency dictionary into a heap


            



