Problem:
Find the longest common prefix in an array of string

Prefix Definition:
First set of characters in a string

Solution:

1. Scan the array O(n) and find the shortest string.

2. Do a for loop through the shortest string length and verify what is the longest sub string that matches every word and append it to the sol array.

3. Keep doing this until a character is not in same position for every string.

4. Return sol array.
