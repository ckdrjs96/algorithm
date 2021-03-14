#bfs
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = collections.deque([root])
        print(queue)
        depth = 0
        print(len(queue))
        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                print(cur_root)
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth