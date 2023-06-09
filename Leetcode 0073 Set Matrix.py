"""
06/19/2023 2:03pm

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        coor = {"x":[], "y":[]}
        ## To find their X, y coor then make in same row and col 0
        for i in range(len(matrix)): 
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    coor["x"].append(i)
                    coor["y"].append(j)
        
        for x in coor['x']:
            for col in range(len(matrix[x])):
                matrix[x][col] = 0
        for y in coor['y']:
            for row in range(len(matrix)):
                matrix[row][y] = 0
