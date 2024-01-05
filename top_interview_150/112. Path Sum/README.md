Problem:
Traverse a binary tree and locate the most sum

    NOTE: Negative numbers included. Binary is not fully binary as 1 branch can be empty

Thought:
Overthought through this problem initially by thinking along the lines of sending back deadendsum with branch sum and comparing while moving up. Realized that this is a bad solution as it became a mess of conditions

    Simplified it by setting maxSum = -1001

    Take the max of existing maxSum and options of root.val,root.val+branches, etc.)

    This solved it but did require refining conditions as the negative # and the empty branches caused some issues.
