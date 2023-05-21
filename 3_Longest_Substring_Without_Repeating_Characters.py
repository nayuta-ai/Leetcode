class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = set()
        left, right = 0, 0
        longest = 0
        for i in range(len(s)):
            right = i
            if s[right] in memo:
                while s[right] != s[left]:
                    memo.remove(s[left])
                    left += 1
                memo.remove(s[left])
                left += 1
            memo.add(s[right])
            longest = max(longest, right-left+1)
        return longest