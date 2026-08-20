# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            answer.append(node.val)
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        answer.sort()
        return answer[k-1]