class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cols = len(grid)
        rows = len(grid[0])

        for i in range(cols):
            for j in range(rows):
                if i==0 and j==0:
                    continue

                elif i==0:
                    grid[i][j] += grid[i][j-1]
                elif j==0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])


        return grid[-1][-1]