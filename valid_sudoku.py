from ast import List

#A) Loop through all rows, storing values as dictionary keys, if the key already exists return false, else add the key
#   Then loop through all columns 
#   Then loop through all sub-boxes 
#   Linear time but the space complexity could definetly be improved
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in board:
            dict = {}
            for y in x:
                if y == ".":
                    continue
                if y in dict:
                    return False
                else:
                    dict[y] = 0
        
        for x in range(len(board)):
            column = [row[x] for row in board]
            dict = {}
            for y in column:
                if y == ".":
                    continue
                if y in dict:
                    return False
                else:
                    dict[y] = 0

        for x in range(3):
            dict1 = {}
            dict2 = {}
            dict3 = {}
            print((1//9 * (x+1)))
            for y in range(27):
                yCoord = self.findYCoord(y)
                num = board[(y // 9) + (x * 3)][yCoord]
                print(num)
                if yCoord <= 2:
                    if num == ".":
                        continue
                    if num in dict1:
                        return False
                    else:
                        dict1[num] = 0
                    print("Dict1")
                    print(dict1)
                elif yCoord >= 3 and yCoord <= 5:
                    if num == ".":
                        continue
                    if num in dict2:
                        return False
                    else:
                        dict2[num] = 0
                    print("Dict2")
                    print(dict2)
                elif yCoord >= 6 and yCoord <= 8:
                    if num == ".":
                        continue
                    if num in dict3:
                        return False
                    else:
                        dict3[num] = 0
                    print("Dict3")
                    print(dict3)
        return True

    def findYCoord(self, y: int) -> int:
        while y > 8:
            y = y - 9
        return y
