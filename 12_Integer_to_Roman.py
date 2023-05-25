class Solution:
    def int_to_roman(self, num: int) -> str:
        roman = ""
        value_symbol = {0:{1:'I', 5:'V'}, 1:{1:'X', 5:'L'}, 2:{1:'C', 5:'D'}, 3:{1:'M'}}

        level = 0
        while num > 0:
            tmp = num % 10
            if tmp < 4:
                while tmp > 0:
                    roman = value_symbol[level][1] + roman
                    tmp -= 1
            elif tmp == 4:
                roman = value_symbol[level][1] + value_symbol[level][5] + roman
            elif 4 < tmp < 9:
                tmp -= 5
                while tmp > 0:
                    roman = value_symbol[level][1] + roman
                    tmp -= 1
                roman = value_symbol[level][5] + roman
            else:
                roman = value_symbol[level][1]+value_symbol[level+1][1]+roman
            level += 1
            num //= 10
        return roman
