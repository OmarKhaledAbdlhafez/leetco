class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_set ={}
        for i in range(len(arr)) :
            if 2*arr[i] in hash_set or arr[i]/2 in hash_set :
                return True
            hash_set[arr[i]] = 2* arr[i]
        