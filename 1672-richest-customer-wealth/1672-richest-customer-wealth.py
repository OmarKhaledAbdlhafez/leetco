class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m =0 
        a =0
        for i in  accounts:
            for j in i :
                a+=j
            if a >m:
                m=a
            a=0    
        
        return m
        