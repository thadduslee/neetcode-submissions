# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q:
            return False
        if q and not p:
            return False
        if not p and not q:
            return True
        
        stack = []
        stack.append([p,q])
        while stack:
            temp1, temp2 = stack.pop()
            if temp2 and not temp1:
                return False
            if temp1 and not temp2:
                return False
            if not temp1 and not temp2:
                continue
            if temp1.val != temp2.val:
                return False
            else:
                stack.append([temp1.left, temp2.left])
                stack.append([temp1.right, temp2.right])
        return True