class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        table = collections.defaultdict(list)

        for x,y in edges:
            table[x].append(y)
            table[y].append(x)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for j in table[i]:
                if j==prev:
                    continue

                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and len(visited)==n