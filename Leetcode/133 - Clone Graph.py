"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def helper(node):
            if not node:
                return node

            if node in self.visited:
                return self.visited[node]

            cloned = Node(node.val, [])
            self.visited[node] = cloned

            if node.neighbors:
                cloned.neighbors = [helper(i) for i in node.neighbors]

            return cloned

        self.visited = {}
        return helper(node)