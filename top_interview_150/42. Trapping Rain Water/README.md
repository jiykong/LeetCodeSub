Problem:
capture the sum of all possible mini puddles

Thought:
this is another array problem that will require left to right and right to left.

Originally attempted to get the sum based on the detection of a basin, but realized a mirror elevation will be an edgecase
Example: [2,0,2]

Realized that if there is a basin then the left and right side scans will have a unison of the min value.

So instead of getting the sum of basin, I opted to simply allocate the value of max - new elevation for possible water flow and got the min of both scans where they joined.

O(n)
