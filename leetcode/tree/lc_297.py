# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    #treenode to list
    def serialize(self, root):

        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque([root])
        ans = []
        while q:
            now = q.popleft()
            if now:
                ans.append(now.val)
            else:
                ans.append(None)
            if now:
                q.append(now.left)
                q.append(now.right)
        # print(ans)
        return ans

    #list to treenode
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        #아무것도 없을 떄 예외 처리리
        if data == [None]:
            return []
        root = TreeNode(data[0])
        q = collections.deque([root])
        i = 1
        while q:
            now = q.popleft()
            # print('now',now,data[i],data[i+1])
            if data[i] != None: #if data[i] 만 하면 값이 0일 때 오류남
                now.left = TreeNode(data[i])
                q.append(now.left)
            if data[i + 1] != None:
                now.right = TreeNode(data[i + 1])
                q.append(now.right)

            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))