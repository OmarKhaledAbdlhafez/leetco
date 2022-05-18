class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenlist = []
        ls =''
        for i in s :
            if i not in ls :
                    ls+=i
            else :
                lenlist.append(len(ls))
                ls = ls [ls.index(i)+1:] +i
                
        lenlist.append(len(ls))
        return max(lenlist)   