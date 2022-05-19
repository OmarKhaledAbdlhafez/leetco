class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c): # return the current area while traversing the island
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1 or (r, c) in visit):
                return 0 # reach the end, the current area is 0
            
            visit.add((r, c))
            return (1 +  # 1 is the current area
                   dfs(r+1, c) + # add the possible adjcent area
                   dfs(r-1, c) +
                   dfs(r, c+1) +
                   dfs(r, c-1) 
                   )
            
        
        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, dfs(r, c)) # compare the area of different islands
        return area            