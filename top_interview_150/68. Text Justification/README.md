Problem:
Text Justification in the worst possible way.

Solution:
Step 1:
Find how many words should minimum fit in a line.

Step 2:
Use modifiers to calculate how many spaces should be allocated.
If mod is == 0, then that means that the number of spaces can be allocated evenly.

    Else, then you have to use the same mod to allocate the extra space while giving the less space to the remainder.

Step 3:
Final line only requires 1 space between word and remainder should be empty.

Comments:
This was not a challenging algo but more of a tedious bug testing problem. I personally didn't like it that much, but was good brain excerecise.
