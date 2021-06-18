class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = ['']
        maxlen = 0

        for i in arr:
            for k in res:
                word = i+k
                if len(word) > len(set(word)):
                    continue
                else:
                    res.append(word)
                    maxlen = max(maxlen, len(word))
        return maxlen