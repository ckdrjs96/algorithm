#dfs
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        global cnt, ans
        ans = 0
        cnt = 0

        def dfs(root):
            global cnt, ans
            if root == None:
                ans = max(ans, cnt)
                return

            cnt += 1
            dfs(root.left)

            dfs(root.right)
            cnt -= 1

        dfs(root)

        return ans