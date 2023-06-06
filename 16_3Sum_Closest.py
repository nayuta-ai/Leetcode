from typing import List


class Solution:
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        curr_closest = float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if abs(target - curr_sum) < abs(target - curr_closest):
                    curr_closest = curr_sum

                if curr_sum < target:
                    j += 1
                elif curr_sum == target:
                    return target

                else:
                    k -= 1
        return curr_closest
