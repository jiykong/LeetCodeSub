class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 1
        i = 0
        if nums[0] >= len(nums)-1:
            return True
        if nums[0] == 0:
            return False
        if(nums == [0]):
            return True

        while i < maxJump:
            if i + nums[i] >= maxJump:
                maxJump = nums[i] + i +1

            if maxJump >= len(nums):
                return True
            i+=1

        return False