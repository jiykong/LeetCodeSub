class Solution:
    def trap(self, height: List[int]) -> int:
        maxElevation = 0;
        totalWater = 0
        possibleWater = 0
        LsolAr = [0]*len(height)
        RsolAr = [0]*len(height)
        firstHeightFound = False;
        counter = 0

        for i in range(len(height)):

            if height[i] < maxElevation:
                LsolAr[i] += (maxElevation - height[i])

            if height[i] >= maxElevation:
                if height[i] > maxElevation:
                    if firstHeightFound:
                        counter+=1
                    else:
                        firstHeightFound=True
                maxElevation = height[i]
                possibleWater = 0
                
        
        maxElevation = 0;
        totalWater = 0
        possibleWater = 0
        
        for i in range(len(height)-1,-1,-1):

            if height[i] < maxElevation:
                RsolAr[i] += (maxElevation - height[i])

            if height[i] >= maxElevation:
                maxElevation = height[i]
                possibleWater = 0


        maxWater = 0
        for i in range(len(height)):
            if(min(LsolAr[i], RsolAr[i]) !=0):
                maxWater += min(LsolAr[i], RsolAr[i])

        return maxWater