# time o(n^2)
# space O(len(numbers)+1)=O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for number in numbers:
            hidden = target
            hidden -= number
            if hidden in numbers[numbers.index(number)+1:]:
                return [numbers.index(number)+1, numbers[numbers.index(number)+1:].index(hidden)+numbers.index(number)+2]