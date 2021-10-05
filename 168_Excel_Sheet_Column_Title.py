# time O(n) n:number of loop
# space O(m) alphabet list:26, out:26^m
import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = list(string.ascii_uppercase)
        out = ''
        alphabet_num = 26
        while columnNumber > 0:
            remainder = columnNumber % alphabet_num - 1
            out = alphabet[remainder] + out
            columnNumber = columnNumber // alphabet_num
            if remainder == -1:
                columnNumber -= 1
        return out