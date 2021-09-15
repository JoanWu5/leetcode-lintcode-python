from typing import List


class Solution:
    def calculateCellState(self, board, x, y, directions):
        live_cells = 0
        m = len(board)
        n = len(board[0])
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0<= nx < m and 0<= ny < n:
                if board[nx][ny] == 1 or board[nx][ny] == -1:
                    live_cells += 1
        
        return live_cells
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                live_cells = self.calculateCellState(board, i, j, directions)
                if board[i][j] == 0:
                    if live_cells == 3:
                        board[i][j] = 2
                else:
                    if live_cells < 2 or live_cells > 3:
                        board[i][j] = -1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1