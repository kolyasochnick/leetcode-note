class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        mn = min(nums)
        mx = max(nums)
        res = []

        count = [0] * (mx - mn + 1)

        for num in nums:
            count[num - mn] += 1
        
        for i in range(len(count)):
            res.extend([i + mn] * count[i])
        
        return sum(res[::2])
            
        