from typing import List


class Solution:
    def __init__(self) -> None:
        self.from_digits_to_letters = {'2':'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.letter_combinations = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.backtracking(digits, "")
        return self.letter_combinations

    def backtracking(self, digits: str, curr_combination: str):
        if not digits:
            self.letter_combinations.append(curr_combination)
            return None

        target = digits[0]
        for char in self.from_digits_to_letters[target]:
            self.backtracking(digits[1:], curr_combination+char)