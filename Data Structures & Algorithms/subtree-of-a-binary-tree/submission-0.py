# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.same(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            


    def same(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        
        if not root2 and root1:
            return False
        
        stack = []
        stack.append([root1, root2])
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            if node1.val != node2.val:
                return False
            
            else:
                stack.append([node1.left, node2.left])
                stack.append([node1.right, node2.right])
        return True