class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        sol_arr = []
        for i in range(len(numbers)):
            if numbers[i] not in hashMap:
                hashMap[numbers[i]] = i
            
            if target-numbers[i] not in hashMap:
                continue; 
            else:
                if hashMap[target-numbers[i]] == i:
                    continue; 
                sol_arr.append(hashMap[target-numbers[i]]+1)
                sol_arr.append(i+1)
                return sol_arr
