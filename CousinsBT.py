class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    # Function to find the parent
    def findParent(self, root, child): 
        if root:
            if root.left and root.left.val == child:
                return root.val
            if root.right and root.right.val == child:
                return root.val
            elif root:
                return self.findParent(root.left, child) or self.findParent(root.right, child)
        
    def getLevelUtil(self, node, data, level):
        if (node == None): 
            return 0
        
        if (node.val == data) : 
            return level  
        
        downlevel = self.getLevelUtil(node.left, data, level + 1)  
        
        if (downlevel != 0) : 
            return downlevel  

        downlevel = self.getLevelUtil(node.right, data, level + 1)  
        
        return downlevel  
  
    def getLevel(self, root, data) : 
        return(self.getLevelUtil(root, data, 1))
    
    # Initial function call after Driver code
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xLevel = self.getLevel(root, x)
        yLevel = self.getLevel(root, y)
        xParent = self.findParent(root, x)
        yParent = self.findParent(root, y)
        
        if xLevel == yLevel and xParent != yParent:
            return True
        else:
            return False
