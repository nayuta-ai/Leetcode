# time complexity: O(n), n is 32
# space complexity: O(1), there is variable (count,n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count