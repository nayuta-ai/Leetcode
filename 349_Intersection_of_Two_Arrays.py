"""
time complexity: O(n) (detailed O(min(len(nums1),len(nums2))))
space complexity: O(n) (detailed O(min(len(nums1),len(nums2))))
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Args:
            nums1 (List[int]): nums1's length is one or more and one thousand or less (0 <= nums1[i] <= 1000)
            nums2 (List[int]): nums2's length is one or more and one thousand or less (0 <= nums2[i] <= 1000)
        Returns:
            List[int]: return the common value between nums1 and nums2
        Examples:
            nums1 = [4, 3, 6, 7], nums2 = [4, 2, 6, 7] -> [4, 6, 7]
        """
        assert len(nums1) != 0, "there is at least one element in nums1"
        assert len(nums2) != 0, "there is at least one element in nums2"
        for i in range(len(nums1)):
            assert nums1[i] >= 0, "the element in nums1 is zero or more integer"
        for i in range(len(nums2)):
            assert nums2[i] >= 0, "the element in nums2 is zero or more integer"
        
        nums12 = set(nums1) & set(nums2)
        return list(nums12)