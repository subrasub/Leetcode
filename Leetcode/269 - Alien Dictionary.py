class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = { ch: set() for w in words for ch in w}

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            mlen = min(len(w1), len(w2))

            if len(w1)>len(w2) and w1[:mlen]==w2[:mlen]:
                return ""

            for j in range(mlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        """
        visited is a hashmap such that it has two values:
        1. False -> means the node has been visited previously
        2. True -> means the node is being visited and is in the current path
        """
        visited = {}
        res = []

        def dfs(ch):
            if ch in visited:
                return visited[ch]

            visited[ch] = True

            for val in adj[ch]:
                if dfs(val):
                    return True

            visited[ch] = False
            res.append(ch)

        for ch in adj:
            if dfs(ch):
                return ""

        res.reverse()
        return ''.join(res)