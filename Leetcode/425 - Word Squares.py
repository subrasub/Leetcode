class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.N = len(words[0])

        res = []
        wordsq = []
        self.buildTable(self.words)

        for word in words:
            wordsq = [word]
            self.backtrack(1, wordsq, res)

        return res

    def backtrack(self, step, wordsq, res):
        if step == self.N:
            res.append(wordsq[:])
            return

        prefix = ''.join([word[step] for word in wordsq])

        for candidate in self.getWordsWithPrefix(prefix):
            wordsq.append(candidate)
            self.backtrack(step+1, wordsq, res)
            wordsq.pop()

    def buildTable(self, words):
        self.prefixTable = {}
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                self.prefixTable.setdefault(prefix, set()).add(word)

    def getWordsWithPrefix(self, prefix):
        if prefix in self.prefixTable:
            return self.prefixTable[prefix]
        else:
            return set([])
