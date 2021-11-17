from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        table = defaultdict(list)

        for course, prereq in prerequisites:
            table[course].append(prereq)

        visited = [0 for _ in range(numCourses)]

        def dfs(i):
            if visited[i] == -1:
                return False

            if visited[i] == 1:
                return True

            visited[i] = -1

            for j in table[i]:
                if not dfs(j):
                    return False

            visited[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True