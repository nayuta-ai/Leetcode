class Solution:
    def roman_to_integer(self, s: str) -> int:
        table = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        ret = 0
        for i in range(len(s)-1):
            if table[s[i]] < table[s[i+1]]:
                ret -= table[s[i]]
            else:
                ret += table[s[i]]
        ret += table[s[len(s)-1]]
        return ret
