class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        global answer

        answer = True

        def dfs(node):
            global answer
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                answer = False
            return max(left, right) + 1

        dfs(root)
        return answer