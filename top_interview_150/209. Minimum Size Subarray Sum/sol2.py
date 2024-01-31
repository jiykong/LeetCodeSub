class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        finalSol = math.inf
        tmpSol = 0
        start = 0
        if sum(nums) < target:
            return 0
            
        total = 0
        for i in range(len(nums)):
            total +=nums[i]
            tmpSol += 1
            while total >= target:
                finalSol = min(finalSol,tmpSol)
                total -= nums[start]
                start+=1
                tmpSol-=1

        return finalSol