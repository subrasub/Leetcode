class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        firstCol = False
        firstRow = False

        for row in range(R):
            for col in range(C):
                if matrix[row][col] == 0:
                    if row == 0:
                        firstRow = True
                    if col == 0:
                        firstCol = True

                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, R):
            for col in range(1, C):
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col] = 0

        if firstRow:
            for col in range(C):
                matrix[0][col] = 0

        if firstCol:
            for row in range(R):
                matrix[row][0] = 0