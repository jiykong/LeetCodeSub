class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solArr = []
        nums.sort()
        i = 0
        
        while i < len(nums)-2:
            target = nums[i]*-1
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue

            j = i + 1
            k = len(nums)-1
            while True:
                if (nums[j] + nums[k]) > target:
                    k-=1
                elif (nums[j] + nums[k]) < target:
                    j+=1
                    
                else:
                    trip=[nums[i],nums[j],nums[k]]
                    solArr.append(trip);
                    while j < k and nums[j] == trip[1]:
                        j +=1;

                if k==j:
                    i += 1
                    break

        return solArr