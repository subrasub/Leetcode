class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        
        def isPalindrome(s):
            if s[::-1] == s:
                return True
            else:
                return False
            
        if s[0] == "":
            return 0
        
        if(isPalindrome(s)):
            return 1
        
        return 2
