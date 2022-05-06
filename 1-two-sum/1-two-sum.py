class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hash_set :
                return [hash_set.get(val) , i]
            hash_set[nums[i]] = i    
            