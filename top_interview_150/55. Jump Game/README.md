Problem:
Jump Problem where you have to ty to solve if an array can jump to the end based on the value in the array's position

NOTE: the number is not a jump count but a max jump count so 2 can jump 1/2

Solution:
Brute force will be to scan each item and each variable, but realized that it is not going to finish the mega test case

Realized that there is a iterative approach where you have a maxJump that as long as it is < length of the array, then we can continue jumping.

Conditioned while loop i < maxjump and adjusted maxjump based on the new value of the array.

If a solution is not found, return default val False.
