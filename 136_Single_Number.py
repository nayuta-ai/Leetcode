# time O(n) n:length of nums
# space O(1)
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common()[-1][0]