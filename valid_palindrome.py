# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

#A) find a way to remove spaces and special characters from the string - O(1) time
#   loop through string and compare "mirrored" characters (first and last, second and second to last, etc)
#   if the characters don't match, return false 0 1 2 3
#   stop loop when at the middle of the string
#   return true

# Initial solution:
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleanString = ''.join(letter for letter in s if letter.isalnum()).lower()
#         length = len(cleanString)

#         if length <= 1:
#             return True

#         for x in range(length):
#             if x >= length - 1 - x:
#                 return True
#             if cleanString[x] != cleanString[length - 1 - x]:
#                 return False
# Runtime
# 54ms
# Beats 60.24%of users with Python3
# Memory
# 17.93MB
# Beats 20.64%of users with Python3

# Going to remove cleanString and store the cleaned string in s as I don't need the old string at all
# I tried storing len(s) in a variable to decrease runtime, but seeing if it really matters

# s = ''.join(letter for letter in s if letter.isalnum()).lower()
#         length = len(s)

#         if length <= 1:
#             return True

#         for x in range(length):
#             if x >= length - 1 - x:
#                 return True
#             if s[x] != s[length - 1 - x]:
#                 return False
# Runtime
# 53ms
# Beats 63.56%of users with Python3
# Memory
# 17.91MB
# Beats 20.64%of users with Python3

# def isPalindrome(self, s: str) -> bool:
#     s = ''.join(letter for letter in s if letter.isalnum()).lower()

#     if len(s) <= 1:
#         return True

#     for x in range(len(s)):
#         if x >= len(s) - 1 - x:
#             return True
#         if s[x] != s[len(s) - 1 - x]:
#             return False
# Runtime
# 51ms
# Beats 70.52%of users with Python3
# Memory
# 17.92MB
# Beats 20.64%of users with Python3

#I might be stupid, but removing a variable increased my memory?!
#Might just be a sample issue ig

#Big gains ig lmao

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(letter for letter in s if letter.isalnum()).lower()

        if len(s) <= 1:
            return True

        for x in range(len(s)):
            if x >= len(s) - 1 - x:
                return True
            if s[x] != s[len(s) - 1 - x]:
                return False