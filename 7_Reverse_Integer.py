class Solution:
    def reverse(self, x: int) -> int:
        max_num = 2**31 - 1
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)

        reverse_integer = 0
        base = 10
        while x > 0:
            curr = x % base
            reverse_integer = reverse_integer*base + curr
            x //= base
        return 0 if reverse_integer > max_num else reverse_integer*sign
