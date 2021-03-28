class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(grid, r, c):
      grid[r][c]='0'
      if((r-1) >= 0 and grid[r-1][c]=='1'):
        dfs(grid, r-1, c)
      if((r+1) < self.rows and grid[r+1][c]=='1'):
        dfs(grid, r+1, c)
      if((c-1) >= 0 and grid[r][c-1]=='1'):
        dfs(grid, r, c-1)
      if((c+1) < self.columns and grid[r][c+1]=='1'):
        dfs(grid, r, c+1)

    self.rows = len(grid)
    self.columns = len(grid[0])

    if(not self.rows or not self.columns):
      return 0

    res = 0

    for r in range(self.rows):
      for c in range(self.columns):
        if(grid[r][c]=='1'):
          res += 1
          dfs(grid, r, c)
    return res
