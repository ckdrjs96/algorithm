# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        global add
        add = 0

        def dfs(node):
            global add
            if not node:
                return

            dfs(node.left)

            if low <= node.val <= high:
                # print('between',node.val)
                add += node.val
            if node.val > high:
                raise ExceptionError

            dfs(node.right)

        try:
            dfs(root)

        except:
            return add

        return add