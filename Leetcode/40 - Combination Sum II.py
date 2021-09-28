class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb, rem, current, counter):
            if rem==0:
                self.res.append(list(comb))
                return
            elif rem<0:
                return

            for i in range(current, len(counter)):
                candidate, freq = counter[i]

                if freq <= 0:
                    continue

                comb.append(candidate)

                counter[i] = (candidate, freq-1)
                backtrack(comb, rem-candidate, i, counter)

                counter[i] = (candidate, freq)
                comb.pop()



        self.res=[]

        counter = Counter(candidates)

        counter = [(c, counter[c]) for c in counter]

        backtrack([], target, 0, counter)

        return self.res