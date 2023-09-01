# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

# Constraints:

# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

#########################################################################################

#A) Constraints eliminate the use of dictionaries, as solution must only take constant space
#   We use a pointer at the end of the array and the beginning, let x be the index at the beginning and y be the index at the end
#   if arr[x] + arr[y] > target, decrement y, since the array is in increasing order, the sum of arr[x] + arr[y - 1] < arr[x] + arr[y] and therefore, closer to the target
#   else if arr[x] + arr[y] < target, increment x for the same reason
#   once arr[x] + arr[y] == target, return [x + 1, y + 1] bc problem uses 1-indexed lists (gross)

from ast import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = 0
        y = len(numbers) - 1
        while(numbers[x] + numbers[y] != target):
            if numbers[x] + numbers[y] > target:
                y-=1
            else:
                x+=1
        return [x + 1, y + 1]