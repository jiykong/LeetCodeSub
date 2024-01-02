class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            k = len(nums)
            return k;

        i = 2
        k = 2
        while i < len(nums):
            if nums[i] == nums[i-1]:
                if nums[k-1] == nums[i] and nums[k-2] != nums[i]:
                    nums[k] = nums[i]
                    k+=1

            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
            i+=1

        return k