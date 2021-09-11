from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        
        result = []
        path = [['.'] * n for _ in range(n)]
        self.dfs(n ,0, path, result)
        return result
    
    def dfs(self, n, row, path, result):
        if row == n:
            result.append(self.convertMatrix(n, path))
            return
        
        for i in range(n):
            path[row][i] = 'Q'
            if self.is_valid(n ,path, row, i):
                self.dfs(n, row + 1, path, result)
            path[row][i] = '.'
            
    def is_valid(self, n, path, row, col):
        for i in range(n):
            if i != row and path[i][col] == 'Q':
                return False
        
        for j in range(n):
            if j != col and path[row][j] == 'Q':
                return False
        
        j = col - 1
        for i in range(row - 1, -1, -1):
            if j < 0:
                break
            if path[i][j] == 'Q':
                return False
            j -= 1
            
        j = col - 1
        for i in range(row + 1, n):
            if j < 0:
                break
            if path[i][j] == 'Q':
                return False
            j -= 1
         
        j = col + 1
        for i in range(row - 1, -1, -1):
            if j >= n:
                break
            if path[i][j] == 'Q':
                return False
            j += 1
            
        j = col + 1
        for i in range(row + 1, n):
            if j >= n:
                break
            if path[i][j] == 'Q':
                return False
            j += 1
        
        return True
        
    def convertMatrix(self, n, path):
        result = []
        for i in range(n):
            line = ''.join(path[i])
            result.append(line)
        
        return result
        
# simplify:
class Solution:
    def solveNQueens(self, n):
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res
 
    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return
        
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                tmp = "."*len(nums)
                self.dfs(nums, index + 1, path + [tmp[: i] + "Q" + tmp[i + 1:]], res)

    def valid(self, nums, index):
        for i in range(index):
            if abs(nums[i] - nums[index]) == index - i or nums[i] == nums[index]:
                return False
        return True     
            