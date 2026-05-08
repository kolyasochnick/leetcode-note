class Solution:

    def _merge(self, nums1, nums2):
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                res.append(nums1[i])
                i += 1
                j += 1
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        q = deque([[x] for x in nums])

        while len(q) > 1:
            left = q.popleft()
            right = q.popleft() if q else []

            q.append(self._merge(left, right))
        
        return q[0] if q else []
        