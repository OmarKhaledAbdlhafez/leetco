class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)<2:
            arr[-1] =-1
        for i in range (len(arr)-1):
            arr[i] = max(arr[i+1:len(arr)])
        arr[-1] =-1
        return arr