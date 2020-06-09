# https://leetcode.com/problems/random-pick-with-weight/
# Tags - Binary Search, Random

class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)): 
            w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        x = random.randint(1, self.w[-1])   
        return bisect.bisect_left(self.w, x)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()