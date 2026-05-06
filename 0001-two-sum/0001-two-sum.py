class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seemed = dict()
        for i, num in enumerate(nums):
            dif = target - num
            if dif not in seemed:
                seemed[num] = i
            else:
                return [seemed[dif], i]


        