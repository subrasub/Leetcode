class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        count = collections.defaultdict(int)
        window = collections.defaultdict(int)

        for ch in t:
            count[ch] += 1

        have, need = 0, len(count)
        res, rlen = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            ch = s[r]

            window[ch] += 1

            if ch in count and count[ch]==window[ch]:
                have += 1

            while have==need:
                if (r - l + 1) < rlen:
                    res = [l, r]
                    rlen = r-l+1

                window[s[l]] -= 1

                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1]