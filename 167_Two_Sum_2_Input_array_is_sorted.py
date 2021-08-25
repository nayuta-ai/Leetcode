# time o(n^2)
# space O(len(numbers)+1)=O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            med = target
            med -= i
            if med in numbers[numbers.index(i)+1:]:
                return [numbers.index(i)+1, numbers[numbers.index(i)+1:].index(med)+numbers.index(i)+2]