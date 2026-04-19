class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        d = {0: 1}
        res = 0
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            res += d.get(s - goal, 0)
            d[s] = d.get(s, 0) + 1

        return res
        