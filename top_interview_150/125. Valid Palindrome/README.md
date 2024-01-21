Problem:
Verify the string is valid palindrome

NOTE: Ignore non-alphanumerics

Solution:

1. set all values to lower.

2. Assign i = 0 and j = last index of array

3. check if any of the value is nonalphanumeric and if so, increment/decrement by 1 for i/j respectively

4. check if value in array in position i / j are the same. If so then increment/decrement by 1 for i/j respectively

5. else return false

6. if the while loop is finished then return True.
