class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(rem, temp, start):
            if rem==0 and len(temp)==k:
                self.res.append(list(temp))
                return
            elif rem < 0 or len(temp)==k:
                return

            for i in range(start, 9):
                temp.append(i+1)
                helper(rem-i-1, temp, i+1)
                # backtrack the current choice because nothing worked
                temp.pop()

        self.res = []
        helper(n, [], 0)
        return self.res
