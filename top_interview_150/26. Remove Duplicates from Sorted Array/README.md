Problem:
There is a sorted array and the goal is to remove duplicates inline.
Meanwhile, count how many unique #s there are

Thought process:
For loop will be required.
Main difference is if the solution should be splicing or if there is a better option...

    Baseline # will be required
    and last instance will also be required to track difference.

Solution 1:
I opted to do a brute force where I initially collected all of the unique items into an array X.
and re run the loop to edit the nums1 to the values in the X in order.

    Problem: this solution is honestly terrible :|

Solution 2:
Althoguh the runtime didn't really improve and was still a hit/miss, the new solution was more elegate

    Instead of double for loop, the new solution continued the original idea of comparing/contrasting.
    Difference was the fact that K was used as the place holder where the edit loc should be as it counts how many unique instance. This was the solution I personally desired.
