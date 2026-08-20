# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if node.left:
                    l = self.height(node.left)
                else:
                    l = 0
                if node.right:
                    r = self.height(node.right)
                else:
                    r = 0
                if abs(l - r) >1:
                    return False
                else:
                    stack.append(node.left)
                    stack.append(node.right)
        return True
    
    def height(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))