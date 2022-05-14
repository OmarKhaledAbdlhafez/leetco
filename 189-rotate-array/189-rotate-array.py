class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #m = len(nums)-1-k
        #nums=nums[m::-1] + nums [:m:-1]
        for i in range(k):
            temp = nums.pop()
            nums.insert(0,temp)