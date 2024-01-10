class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solArr = [1] * len(nums)
        
        forward = [1] * (len(nums)-1)
        backward = [1] * (len(nums)-1)

        for i in range(len(nums)-1):
            if i ==0:
                forward[i] = nums[i]

            else:
                forward[i]=(nums[i] * forward[i-1])

        for i in range(len(nums)-1,0,-1):
            if i == (len(nums)-1):
                backward[i-1]=(nums[i])

            else:
                backward[i-1]=(backward[i] * nums[i])
                
        for i in range(len(solArr)):
            if i == 0:
                solArr[i] = backward[i]

            elif i == (len(solArr)-1):
                solArr[i] = forward[len(forward) - 1]
            
            else:
                solArr[i] = forward[i-1]*backward[i]
        return solArr