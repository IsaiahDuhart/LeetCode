# Description
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Example
# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"
# Example2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"
from ast import List

#A) Convert each string to it's ascii code separated by commas, words are separated by semi-colons
#Not Tested yet
class Solution:
    """
     @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs: List[str]) -> str:
        ret = ""
        for x in strs:
            ret = ret + x.encode() + ";"
            ret = ret + ";"
        return ret
            

    """
   @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str: str) -> List[str]:
        ret = str.split(";")
        for x in ret:
            x = x.decode("utf-8")