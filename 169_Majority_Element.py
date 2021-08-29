# space O(n)
# time O(n)
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return c.most_common()[0][0]