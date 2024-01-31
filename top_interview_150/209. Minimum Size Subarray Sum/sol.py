class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        finalSol = math.inf
        tmpSol = 0
        total = 0

        trackingAr = []
        for num in nums:
            tmpSol+=1
            total+=num
            trackingAr.append(num)

            while total >= target:
                if tmpSol < finalSol:
                    finalSol=tmpSol
                total-=trackingAr[0]
                trackingAr.pop(0)
                tmpSol-=1
                if len(trackingAr) == 0:
                    break;
        if finalSol == math.inf:
            return 0
        return finalSol
