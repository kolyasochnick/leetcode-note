class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = str(n)
        x = '0'
        sums = 0
        for digit in n:
            if digit != '0':
                x += digit
                sums += int(digit)
        
        return int(x) * sums



        