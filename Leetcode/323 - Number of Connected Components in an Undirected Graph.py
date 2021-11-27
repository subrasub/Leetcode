class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(n, table, visited):
            if visited[n]:
                return

            visited[n] = 1
            for v in table[n]:
                dfs(v, table, visited)


        table = {i:[] for i in range(n)}
        visited = [0] * n

        for x, y in edges:
            table[x].append(y)
            table[y].append(x)

        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, table, visited)
                res += 1

        return res