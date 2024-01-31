class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxContainer = 0;

        i = 0 
        j = len(height) - 1

        while i < j:
            maxContainer= max(min(height[i],height[j]) * (j-i),maxContainer) 
            if height[i] <= height[j]:
                i+=1 

            else:
                j-=1

        return maxContainer