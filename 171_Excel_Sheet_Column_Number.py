# time O(n) n:len(columnTitle)
# space O(m) m:length of alphabet list
import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = list(string.ascii_uppercase)
        length = len(columnTitle)
        ans = 0
        alphabet_num = 26
        for i in columnTitle:
            ans = (alphabet.index(i) + 1) * alphabet_num ** (length - 1) + ans
            length = length - 1
        return ans