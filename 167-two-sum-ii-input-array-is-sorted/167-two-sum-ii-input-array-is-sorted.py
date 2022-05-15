class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_set ={}
        for i in range(len(numbers)):
            val = target - numbers[i]
            if val in hash_set :
                return [hash_set.get(val)+1 , i+1]
            else :
                hash_set[numbers[i]]=i