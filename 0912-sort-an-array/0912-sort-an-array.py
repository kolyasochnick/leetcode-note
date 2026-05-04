class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def radixSort(nums, negative=False):
            if not nums:
                return nums
            if negative:
                nums = [-num for num in nums]
            place = 1
            maxElem = max(nums)

            while maxElem // place > 0:
                buckets = [[] for _ in range(10)]

                for num in nums:
                    index = (num // place) % 10
                    buckets[index].append(num)

                nums = [num for bucket in buckets for num in bucket]
                place *= 10
            if negative:
                return [-num for num in nums][::-1]
            return nums
        positive = radixSort(list(filter(lambda x: x>=0, nums)))
        negative = radixSort(list(filter(lambda x: x<0, nums)), True)

        return negative + positive

