# https://leetcode.com/problems/is-subsequence/
# Tags - Greedy, Binary Search, Dynamic Programming

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = collections.deque(s)
        
        for letter in t:
            if not queue:
                return True
            if letter == queue[0]:
                queue.popleft()
            
        return len(queue)==0