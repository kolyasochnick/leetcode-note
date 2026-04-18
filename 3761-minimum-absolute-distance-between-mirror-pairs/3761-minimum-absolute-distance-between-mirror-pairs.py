class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        hashmap = dict()
        res = len(nums)
        for i, num in enumerate(nums):
            rev = int(str(num)[::-1])
            if num in hashmap:
                res = min(res, i - hashmap[num])
            hashmap[rev] = i
            
        if res == len(nums):
            return -1
        return res

        