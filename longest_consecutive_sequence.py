# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

from ast import List

#A) Create a dictionary that stores elements, check if the element - 1 is a key, if so, update key to element and increment value, also keep track of largest value - O(n) time
#   return largest value
#   Doesn't work unless values are added sequentially i.e. (1,2,3,4) doesn't work if numbers are scrambled like (2,4,1,3)
#B) Split list into connect component sequences 
#   Create a dictionary that stores elements as keys and values that are lists of the connected component sequence, if the element is a key, skip the element,
#   if not, check if the element - 1 or element + 1 is a key, if so, update key to element and add the element to the list, also keep track of largest value,
#   if both el +- 1 are keys, combine the list - O(n) time
#   
#   It passes, but it isn't that fast and takes up a TON of memory
#   Possible improvements:
#   Only store the greatest and smallest numbers of the sequence in the list, then when a new element is added, you know which other list to update (only the key on the other side of the sequence)
#   With this approach, only subtract the second element from the first to find the length of the sequence
#
#   This update reduced my memory usage by 10 mbs (Which was only a 19.9% reduction), but it increased my runtime by 40 ms (11% slowdown) :(
#       This solution is very bad, which makes me sad. But im moving on, which makes me happy
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        largestSeq = 0
        smallestNum = 0
        greatestNum = 0
        for x in nums:
            if x in dict:
                continue
            if x-1 in dict and x + 1 in dict:
                greatestNum = x + dict[x + 1][1]
                smallestNum = x - dict[x - 1][0]
                dict[greatestNum] = [dict[smallestNum][0], dict[greatestNum][1]]
                dict[smallestNum] = dict[greatestNum]
                dict[x] = None
                
            elif x - 1 in dict:
                dict[x] = dict[x-1]
                dict[x][1] = x
                dict[dict[x][0]][1] = x
                if len(dict[x]) >= 3:
                    dict[x - 1] = None
                greatestNum = x
                smallestNum = dict[x][0]
            elif x + 1 in dict:
                dict[x] = dict[x + 1]
                dict[x][0] = x
                dict[dict[x][1]][0] = x
                if len(dict[x]) >= 3:
                    dict[x + 1] = None
                smallestNum = x
                greatestNum = dict[x][1]
            else:
                dict[x] = [x, x]

            if dict[smallestNum][1] >= 0:
                thisSeq = dict[smallestNum][1] - dict[smallestNum][0] + 1
                if largestSeq < thisSeq:
                        largestSeq =  thisSeq
            else:
                thisSeq = -dict[smallestNum][1] + dict[smallestNum][0] + 1
                if largestSeq < thisSeq:
                    largestSeq = thisSeq
        return largestSeq