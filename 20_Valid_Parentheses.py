class ValidParentheses:
    def is_valid(self, s: str) -> bool:
        from_left_to_right = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char not in from_left_to_right:
                stack.append(char)
            else:
                if not stack:
                    return False

                left_parenthes = stack.pop()
                if from_left_to_right[char] != left_parenthes:
                    return False

        return not stack