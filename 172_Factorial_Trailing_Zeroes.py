# time O(1)
# space O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        for i in range(1,6):
            if n < 5 ** i:
                break;
                
            cnt = cnt + n // (5 ** i)
        return cnt