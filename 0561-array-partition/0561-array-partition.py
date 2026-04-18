class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                a = num
            else:
                res += min(a, num)
        return res
            
        