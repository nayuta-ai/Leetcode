# time complexity: O(k*m), k = 50, m is length variable n
# space complexity: O(1), there is variable jud, cnt, n, n_sum
class Solution:
    def isHappy(self, n: int) -> bool:
        jud = False
        cnt = 0
        while cnt < 50:
            n_sum = 0
            while n > 0:
                n_sum += (n % 10) ** 2
                n = n // 10
            n = n_sum
            cnt += 1
            if n == 1:
                jud = True
                break;
        return jud