class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ## searching for the instance of K
        instance_of_val = 0

        ## searching where to start the for loop
        startofArr = 0

        ## searching where to end the for loop
        endofArr = len(nums)-1

        ## while loop to go in place of a for loop
        while startofArr <= endofArr:
            ## instance ++
            if nums[startofArr] == val:
                instance_of_val+=1;

                ## switching the values of the end of array with start of array val
                tmpVal = nums[endofArr]
                nums[endofArr] = nums[startofArr]
                nums[startofArr] = tmpVal

                ## decrementing the end of array down as anything past is now set properly
                endofArr-=1;

            
            ## start of array moving up.
            else: 
                startofArr+=1;

        ## locating array location where val starts.
        arrayLoc = len(nums) - instance_of_val

        return  arrayLoc
        