class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return

        center = (len(nums)) // 2

        Node = TreeNode(nums[center])
        Node.left = self.sortedArrayToBST(nums[:center])
        Node.right = self.sortedArrayToBST(nums[center + 1:])

        return Node
