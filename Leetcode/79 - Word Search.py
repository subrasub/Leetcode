# https://leetcode.com/problems/word-search/
# Tags - Array, Backtracking

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, curr):
            if curr == len(word):
                return True
            
            if (r<0 or c<0 or r>=ROWS or c>=COLS or
                word[curr] != board[r][c] or (r,c) in path):
                return False
            
            path.add((r,c))
            res = (
                dfs(r+1, c, curr+1) or
                dfs(r-1, c, curr+1) or
                dfs(r, c+1, curr+1) or
                dfs(r, c-1, curr+1)
            )
            path.remove((r, c))
            return res
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.R, self.C = len(board), len(board[0])
        self.board = board
        
        for row in range(self.R):
            for col in range(self.C):
                if self.find(word, row, col):
                    return True
        
        return False
    
    def find(self, term, row, col):
        if not len(term):
            return True
        
        if row<0 or col<0 or row==self.R or col==self.C or self.board[row][col] != term[0]:
            return False
        
        self.board[row][col] = '*'
        
        for moveRow, moveCol in [(0,1), (1, 0), (0, -1), (-1, 0)]:
            val = self.find(term[1:], row + moveRow, col + moveCol)
            if val:
                break
        
        self.board[row][col] = term[0]
        
        return val
        