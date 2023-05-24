from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            area = max(area,(right - left) * min(height[left], height[right]))
        return area
