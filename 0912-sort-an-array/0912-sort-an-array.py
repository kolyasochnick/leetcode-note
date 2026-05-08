class Solution:
    def _radixSort(self, nums):
        if not nums:
            return []
        dec = 1
        maxEl = max(nums)
        while maxEl // dec > 0:
            buckets = [[] for _ in range(10)]
            for num in nums:
                index = (num // dec) % 10
                buckets[index].append(num)
            nums = [num for bucket in buckets for num in bucket]
            dec *= 10
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:

        positive = self._radixSort(list(filter(lambda x: x >= 0, nums)))
        negative = [-x for x in self._radixSort([-x for x in nums if x < 0])][::-1]

        return negative + positive
        