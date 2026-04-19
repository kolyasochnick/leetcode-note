class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        res = 0
        s = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                s += 1
            else:
                s -= 1
            if s in d:
                res = max(res, i - d[s])
            else:
                d[s] = i

        return res
