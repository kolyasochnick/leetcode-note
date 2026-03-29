from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        point1 = 0
        point2 = 0
        
        res = []
        while point1 < len(nums1) and point2 < len(nums2):
            if nums1[point1] == nums2[point2]:
                res.append(nums1[point1])
                point1 += 1
                point2 += 1
            elif nums1[point1] > nums2[point2]:
                point2 += 1
            else: 
                point1 += 1
        return res


        
                