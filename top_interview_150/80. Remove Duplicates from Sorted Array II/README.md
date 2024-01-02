Problems:
Branch of the original remove duplicate from sorted array ii

Key difference is that the you can have 2 instances of the duplicates in the resulting nums.

Thought Process:

It is the same solution except an extra condition so far.

Solution1:
As expected, the solution was similar to sorted array 1 except the following.
  
 1. Base condition of len(nums) was required as anything less than 3 element was simply the return of the len as K and no edit to nums

    2. Extra conditionals were required when the duplicates were found to search if duplicates already exist in last 2 values of K

    3. other than that, it was a normal procedure.

    4. The runtime is not as good so there is a better solution probably that I will research.
