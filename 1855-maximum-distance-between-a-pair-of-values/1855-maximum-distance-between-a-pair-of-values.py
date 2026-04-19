class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = len(nums1) - 1
        j = len(nums2) - 1
        res = 0
        while i >= 0:
            if i <= j:
                if nums1[i] <= nums2[j]:
                    res = max(res, j - i)
                    i -= 1
                else:
                    j -= 1
            else:
                i = j
                res = max(res, j - i)
        return res
            

