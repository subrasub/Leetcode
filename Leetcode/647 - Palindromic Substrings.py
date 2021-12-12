class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(s, lo, hi):
            cnt = 0

            while lo>=0 and hi<len(s):
                if s[lo]!=s[hi]:
                    break
                lo -= 1
                hi += 1
                cnt += 1

            return cnt

        res = 0

        for i in range(len(s)):
            res += helper(s, i, i)      #even
            res += helper(s, i, i+1)    #odd


        return res