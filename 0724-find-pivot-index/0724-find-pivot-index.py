class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            j = n - i - 1
            left[i] = left[i - 1] + nums[i]
            right[j] = right[(j + 1) % n] + nums[j]
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1