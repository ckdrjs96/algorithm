class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        def dfs(node1, node2):

            if node1 and node2:

                node = TreeNode(node1.val + node2.val)
                node.left = dfs(node1.left, node2.left)
                node.right = dfs(node1.right, node2.right)

                return node
            else:
                return node1 or node2

        return dfs(root1, root2)