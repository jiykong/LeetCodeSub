Description
    Longest String with non repeating characters

Thought:

The concept is the same and the scan will be linear.

While doing a linear scan, you have to store the first unique instance of each char into a hash map with the value of its location.

If a duplicate is found, then operation must be done to check and possibly save the new longest string value.

At the end of the day save the finalSol.

Solution:

Had to add a start checker due to edge case where if duplicate exist before the start of the word.

There was still a bug until I realized that you had re-update the mapper every time there is a duplicate regardless of previous edgecase.