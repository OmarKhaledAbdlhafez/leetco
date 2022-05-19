class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        h = len(grid)
        w = len(grid[0])
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid,i,j)
                    
        return count
    
    def dfs(self,grid,i,j):
        h = len(grid)
        w = len(grid[0])  
        
        if i<0 or j<0 or i>=h or j>=w:
            return
        
        if grid[i][j] != '1':
            return
        
        grid[i][j] = '#'
        
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)