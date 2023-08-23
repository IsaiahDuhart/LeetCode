from ast import List

#My original thought was to simply find the product of the array, and fill in the return array by finding the quotient of the product/nums[i].
#However, the question descripiton included "You must write an algorithm that runs in O(n) time and without using the division operation.",
#So I used my original approach but divided by multiplying by the divisor raised to the negative first power.
#There are probably ways to do this problem without using any sort of division or tricks to use it anyways, but im not smart enough to find them, so this is my approach
#O(n) solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0
        prod = 1
        ret = []
        for x in nums:
            if x == 0:
                numZeros += 1
                if numZeros == 1:
                    continue
            prod = prod * x

        if prod == 0:
            return [0] * (len(nums))
        
        for x in nums:
            if numZeros == 1:
                if x == 0:
                    ret.append(prod)
                else:
                    ret.append(0)
                continue
            ret.append(int(prod * (x**-1)))

        return ret