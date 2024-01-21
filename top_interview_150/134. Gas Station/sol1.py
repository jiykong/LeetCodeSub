class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        netTank = []
        
        for i in range(len(gas)):
            netTank.append(gas[i]-cost[i])
        
        if len(netTank) == 1:
            if netTank[0] >=0:
                return 0
            else:
                return -1
        tmpmaxProfit = 0
        maxProfit = 0

        rotations = 0
        startingLoc = -1
        startingLocFound = False
        i = 0
        while True:
            if rotations == 2 and i==0:
                return -1

            if startingLoc == i and startingLocFound==True:
                return i;

            if i == len(netTank):
                i = 0
                rotations+=1
                continue

            else:
                tmpmaxProfit = maxProfit + netTank[i]
                if tmpmaxProfit <= 0:
                    if tmpmaxProfit==0:
                        tmpi = i + 1
                        if tmpi == len(netTank):
                            tmpi = 0
                        if tmpi == startingLoc and startingLocFound==True:
                            return tmpi
                        
                    i+=1;
                    maxProfit=0
                    startingLocFound=False
                    continue;

                else:
                    if startingLocFound==False:
                        startingLoc = i
                        startingLocFound=True
                    maxProfit = tmpmaxProfit
                    i+=1;

        return -1