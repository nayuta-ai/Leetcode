class Solution:
    def longest_palindrome(self, s: str) -> str:
        def curr_longest_palindrome(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        longest = ""
        for i in range(len(s)):
            substring = curr_longest_palindrome(i, i)
            if len(substring) > len(longest):
                longest = substring

            substring = curr_longest_palindrome(i, i+1)
            if len(substring) > len(longest):
                longest = substring

        return longest
