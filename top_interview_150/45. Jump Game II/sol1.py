class Solution:
    def jump(self, nums: List[int]) -> int:
        jumpCount = 0
        maxJump = 1
        i = 0
        tmpMaxJump = 0
        if len(nums) == 1:
            return 0



        while i < len(nums):
            if(i+nums[i]+1 >= len(nums)):
                jumpCount+=1
                return jumpCount
            subArray = nums[i+1:nums[i]+i+1]
            maxPossibleJump = 0
            maxPossibleJumpLoc = -1
            for j in range(len(subArray)):
                if (subArray[j] - (len(subArray) - (j + 1))) > maxPossibleJump:
                    maxPossibleJump = subArray[j] - (len(subArray) - (j + 1))
                    maxPossibleJumpLoc = i + j + 1

            jumpCount+=1
            i = maxPossibleJumpLoc
        return jumpCount
            
