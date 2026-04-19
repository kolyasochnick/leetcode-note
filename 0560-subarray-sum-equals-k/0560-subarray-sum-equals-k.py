class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res = 0
        s = 0
        for num in nums:
            s += num
            res += count[s - k]
            count[s] += 1
        return res