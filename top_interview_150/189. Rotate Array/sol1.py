class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = (k % len(nums))
        if k == 0:
            return nums
        rotatedList2 = nums[0:len(nums)-k]
        nums[0:len(nums)-k] = nums[len(nums)-k:]
        nums[len(nums)-k:] = rotatedList2