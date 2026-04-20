class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left = 0
        right = len(colors) - 1

        while colors[left] == colors[right]:
            right -= 1
        
        res = right - left

        left = 0
        right = len(colors) - 1
        while colors[left] == colors[right]:
            left += 1
        
        return max(res, right - left)

        