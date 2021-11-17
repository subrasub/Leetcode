class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            node = node.children[ch]

        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        self.res = False
        self.dfs(node, word, 0)
        return self.res

    def dfs(self, node, word, i):
        if len(word) <= i:
            if node.isWord:
                self.res = True
            return

        if word[i]=='.':
            for n in node.children.values():
                self.dfs(n, word, i+1)
        else:
            node = node.children[word[i]]
            if not node:
                return
            self.dfs(node, word, i+1)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)