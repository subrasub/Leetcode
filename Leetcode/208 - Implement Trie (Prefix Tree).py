class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]

        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root

        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]

        return node.isWord


    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)