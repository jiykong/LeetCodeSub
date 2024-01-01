Problem:
Given an array of numbers, remove any instances of val.

While removing, count how many instances of val and return the count

meanwhile return the array such that the all of the numbers != val is first in the list.

Thought process:
The solution seems to be simple.
Establish baseline param of empty array and baseline value
Read through the array, count how many instances of val.
Meanwhile append values not == to val into the empty array.
switch nums with the new array.

Limitations, Realized the request is that the value be in line

Found out later that the k value isn't the # of instance of value but the array location where the instance of val will begin in the new array.

Solution:
Simple while loop to search through the array for any val.

During the switch a the start / end value of array will slide.

If item == val, then the end of array will slide left after performing a switch
else, then the start of array will slide right
