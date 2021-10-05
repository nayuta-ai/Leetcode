# time complexity: o(n), n = 32
# space complexity: o(n), n = 32
class Solution:
    def reverseBits(self, n: int) -> int:
        sum_reverse = 0
        for i in range(32):
            sum_reverse += (n % 2) * 2 ** (31-i)
            n = n // 2
        return sum_reverse