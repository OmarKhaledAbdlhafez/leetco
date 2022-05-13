class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        num = nums.copy()
        r = len(nums)-1
        l=0
        for i in range(len(num)):
            if (num[i]%2 !=0):
                nums[r] = num[i]
                r -= 1
            else :
                nums[l]= num[i]
                l+=1
        return nums