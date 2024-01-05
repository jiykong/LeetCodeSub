Problem: get the max profit in an array.

Thought Process:

Originally thought through this problem in a way that beginning index vs ending index that searches out the max value.

This is not a proper solution and therefore will try an initial brute force to see what can be eliminated

I then attempted brute force, but brute force is not possible as there is a time complexity limit.

Gave up and went to sleep but woke up next day and realized that we can store sequential max profits.

Store possible max profit and slowly iterate through it one by one until the end of the array and return whatever was found to be the max profit.
