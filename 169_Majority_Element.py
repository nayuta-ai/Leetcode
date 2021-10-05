# space O(n) n is length of list nums
# time O(n) n is length of list nums
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common()[0][0]