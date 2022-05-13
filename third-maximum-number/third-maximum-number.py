class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numset = list(set(nums))
        if len(numset)<3:
            return max(numset)
        else :
            return sorted(numset)[-3]
            
       