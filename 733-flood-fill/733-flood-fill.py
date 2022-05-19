class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        start = image[sr][sc]
        self.dfs(image, sr,sc,newColor,start)
        
        
        return image
    def dfs (self,image, sr,sc,newColor,start) :
        
        if sr <0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc]==newColor or image[sr][sc] != start :
            return 
            
        image[sr][sc] = newColor
        self.dfs(image,sr+1,sc,newColor,start)
        self.dfs(image,sr-1,sc,newColor,start)
        self.dfs(image,sr,sc+1,newColor,start)
        self.dfs(image,sr,sc-1,newColor,start)
            