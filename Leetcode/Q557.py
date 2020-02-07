class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
            
        return ' '.join([rev[::-1] for rev in s])
