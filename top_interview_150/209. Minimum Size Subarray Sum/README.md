Description:
    Find the lowest amount of numbers that will add up to be == or > than target #

Thought:
    Solution is pretty simple, sort, and then just scan from right -> left and count.

    Realized the subarray meant that you cannot sort the original array to get the solution.

    Initial Solution used involved a for loop through each number while appending the number to the sliding window trackingAr

    THe goal was to shrink the trackingAr and while the size of total > target while saving the smallest tmpsol in the finalsol

    This solution is very bad runtime as it could theoretically mean it is taking quadratic time.

2ndThought Solution:

    I realized the main issue was that i was treating the array as the window while you can handle the array in place.

    
