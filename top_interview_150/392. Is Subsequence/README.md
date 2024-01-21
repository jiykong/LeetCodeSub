Problem:
Check if string is subsequenced.

Solution:
Doing the special case solution.

    1. Create a hash map and list all character occurence of string T inside the hashmap in form of hashmap[char] = [list of occurences]

    2. Scan through s and validate if chharacter is in the hashmap and then check if the value is properly subsquenced.

    3. If any failures are found, then return false.
