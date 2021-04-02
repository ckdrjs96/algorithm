# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        global mindiff, before
        mindiff = float('inf')
        before = -float('inf')

        def dfs(node):
            global mindiff, before
            if not node:
                return

            dfs(node.left)
            mindiff = min(mindiff, node.val - before)
            # print(node.val,node.val-before)
            before = node.val
            dfs(node.right)

        dfs(root)
        return mindiff