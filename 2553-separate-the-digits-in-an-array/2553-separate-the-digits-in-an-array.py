class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in reversed(nums):
            while num // 10 > 0:
                add = num % 10
                res.append(add)
                num //= 10
            res.append(num)
        return res[::-1] 
        