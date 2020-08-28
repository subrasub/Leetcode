class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.rev(0, len(s)-1, s)
        
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.rev(start, i-1 , s)
                start = i+1
            elif i == len(s)-1:
                self.rev(start, i, s)
        
        
    def rev(self, left, right, s):
        while left < right:  
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1