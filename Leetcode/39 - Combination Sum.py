class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(rem, temp, start):
            if rem==0:
                self.res.append(list(temp))
                return
            elif rem < 0:
                return

            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                helper(rem-candidates[i], temp, i)
                # backtrack the current choice because nothing worked
                temp.pop()

        self.res = []
        helper(target, [], 0)
        return self.res