class Solution:
  def longestPalindrome(self, s: str) -> str:
    def expand(left, right):
      while left>=0 and right<len(s) and s[left]==s[right]:
        if (right-left+1) > len(self.res):
          self.res = s[left:right+1]
        left -= 1
        right += 1

    self.res = ""

    for i in range(len(s)):
      expand(i, i)
      expand(i, i+1)

    return self.res