#trie
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for val in word:
            node = node.children[val]
        # print(node.children)
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for val in word:
            # print(node.children)
            if val not in node.children:
                return False
            node = node.children[val]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        # print(node)
        for val in prefix:
            if val not in node.children:
                return False
            node = node.children[val]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)