class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def in_order_traversal(self, r):
        if r == None: return [ ]
        return [*self.in_order_traversal(r.left), r.val, *self.in_order_traversal(r.right)]
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if (s == None or t == None): return False
        if s.val == t.val and self.in_order_traversal(s) == self.in_order_traversal(t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
