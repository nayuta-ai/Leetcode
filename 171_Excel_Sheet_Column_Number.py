# time O(n) n:len(columnTitle)
# space O(m) m:length of alphabet list
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = [chr(i) for i in range(65,65+26)]
        length = len(columnTitle)
        ans = 0
        for i in columnTitle:
            ans = (alphabet.index(i) + 1) * 26 ** (length - 1) + ans
            length = length - 1
        return ans