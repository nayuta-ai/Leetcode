class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse_integer = 0
        curr = x
        while curr > 0:
            reverse_integer = reverse_integer * 10 + curr % 10
            curr //= 10
        return x == reverse_integer
