class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        dif = max(nums) - min(nums) + 1
        count = [0] * dif
        for num in nums:
            count[num - mn] += 1
        
        res = []
        for i in range(dif):
            value = i + mn

            for _ in range(count[i]):
                res.append(value)
                
        return res

