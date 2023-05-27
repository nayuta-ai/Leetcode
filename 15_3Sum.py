from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        three_sum_pairs = []
        for i in range(len(nums)-2):
            if i >= 1 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    three_sum_pairs.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1

                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return three_sum_pairs