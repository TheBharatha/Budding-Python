class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
            
            if leftHeight > rightHeight:
                return(leftHeight+1)
            else:
                return(rightHeight+1)