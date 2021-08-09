class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]
# Runtime 40ms
# Momory 14.9MB