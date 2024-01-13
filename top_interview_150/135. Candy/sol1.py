class Solution:
    def candy(self, ratings: List[int]) -> int:
        solAr = [1] * len(ratings)

        for i in range(len(solAr)-1):
            if ratings[i+1] > ratings[i] and solAr[i+1] <= solAr[i]:
                solAr[i+1] = solAr[i] + 1

        for i in range(len(solAr) - 1, 0,-1):
            if ratings[i-1] > ratings[i] and solAr[i-1] <= solAr[i]:
                solAr[i-1] = solAr[i] + 1

        return sum(solAr) 
    