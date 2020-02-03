class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if not palindrome:
            return ""
        
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[(i+1):]
        
        if palindrome[:-1]:
            return palindrome[:-1] + 'b'
        else:
            return ""
            
