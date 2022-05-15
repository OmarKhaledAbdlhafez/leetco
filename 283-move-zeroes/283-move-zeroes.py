class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = nums.copy()
        r = len(nums)-1
        l=0
        for i in range(len(num)):
            if (num[i]==0):
                nums[r] = num[i]
                r -= 1
            else :
                nums[l]= num[i]
                l+=1