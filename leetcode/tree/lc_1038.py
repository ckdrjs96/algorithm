# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        global add
        add = 0

        def bfs(root):
            global add
            if not root:
                return

            bfs(root.right)

            add += root.val
            root.val = add

            bfs(root.left)

        bfs(root)
        return root