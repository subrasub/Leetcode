class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        top = 0
        bottom = R-1

        while top <= bottom:
            mid = top + (bottom-top)//2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        # if target is out of bounds
        if not top<=bottom:
            return False

        row = top + (bottom-top)//2
        left, right = 0, C-1

        while left<=right:
            mid = left + (right-left)//2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
