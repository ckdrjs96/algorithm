

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return

        #전위순회의 제일 앞갚을 노드로 지정
        root = preorder[0]
        i = inorder.index(root)
        node = TreeNode(root)

        inorder_next = inorder[:i + 1]
        inorder_next.remove(root)
        node.left = self.buildTree(preorder[1:i + 1], inorder_next)
        node.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])

        return node