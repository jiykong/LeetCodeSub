Problem:
Same but now we have to count the minimum jump possible

Thought:
I think we just need to add a jump counter and adjust it each time maxjump reaches the end of the array.

If new jump counter < then great, else no

Trickier as I realized that simply jumping like previously won't solve the problem.

Instead i used a sliding box trick where I get the maximum possible "True Jump within a range of the jump and check after each sliding box if the value reached the endzone.
