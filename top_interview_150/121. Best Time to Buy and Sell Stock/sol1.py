class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        miniProfits = []
        
        for i in range(len(prices) - 1):
            miniProfits.append((prices[i] - prices[i+1])*-1)

        tmpmaxProfit = 0
        maxProfit = 0

        for i in range(len(miniProfits)):
            tmpmaxProfit = max(0,(tmpmaxProfit + miniProfits[i]))
            if tmpmaxProfit > maxProfit:
                maxProfit = tmpmaxProfit

        return maxProfit