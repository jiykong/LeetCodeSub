Description
Find the largest possible container within a set of array.

Thought:
Brute force would be for each item in array to do a box calc for every other item in array.

This is quadratic so not good.

Instead of that, you have to scan from left to right and right to left simultaneously.

While doing so, new maxcontainer should be constantly calculated.

Key is that you increment i and decrement j based on the value so that the larger side stays the same while the smaller side moves to calculate the largest possible box.