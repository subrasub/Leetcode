class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix, n):
            for i in range(n):
                for j in range(i, n):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

        def reverse(matrix, n):
            for i in range(n):
                for j in range(n//2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i][-j-1]
                    matrix[i][-j-1] = temp

        n = len(matrix)
        transpose(matrix, n)
        reverse(matrix, n)
