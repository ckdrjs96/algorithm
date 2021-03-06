# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        global cnt
        cnt = 0

        def dfs(root):
            global cnt
            if root == None:
                return -1, -1

            a1, a2 = dfs(root.left)
            b1, b2 = dfs(root.right)
            now = root.val
            a = max(a1, a2) + 1
            b = max(b1, b2) + 1

            if root.left and root.left.val != now:
                a = 0
            if root.right and root.right.val != now:
                b = 0

            cnt = max(cnt, a + b)
            return a, b

        dfs(root)
        return cnt