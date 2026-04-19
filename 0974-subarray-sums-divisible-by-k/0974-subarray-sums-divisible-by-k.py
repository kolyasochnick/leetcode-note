class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        res = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            res += d.get(s % k, 0)
            d[s % k] = d.get(s % k, 0) + 1
        return res       