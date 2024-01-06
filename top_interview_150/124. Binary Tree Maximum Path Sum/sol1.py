# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

maxSum = -1001


def recur(root):
    global maxSum
    if not root.left and not root.right:
        return root.val;
    else:
        if root.left:
            leftSum = recur(root.left)
        if root.right:
            rightSum = recur(root.right)
    
    if root.left==None:
        maxSum = max(maxSum, root.val,rightSum,rightSum+root.val)
        return(max(rightSum + root.val,root.val))
    
    elif root.right==None:
        print(leftSum)
        maxSum = max(maxSum, root.val, leftSum,leftSum+root.val)
        return(max(leftSum + root.val,root.val))

    else:
        maxSum = max(maxSum, root.val, leftSum,rightSum,leftSum+root.val,rightSum+root.val,leftSum+rightSum+root.val)
        return(max(max(leftSum,rightSum) + root.val,root.val))


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global maxSum      
        maxSum=-1001
        if not root.left and not root.right:
            return root.val;
        recur(root)

        return(maxSum)