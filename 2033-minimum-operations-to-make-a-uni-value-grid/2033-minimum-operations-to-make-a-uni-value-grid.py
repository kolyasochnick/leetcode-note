class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        q = set()
        nums = []
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                q.add(grid[i][j] % x)
                if len(q) > 1:
                    return -1
                nums.append(grid[i][j])
        
        nums.sort()
        print(nums)
        mid = nums[len(nums) // 2]

        res = 0
        for num in nums:
            res += abs(num - mid) // x

        return res 




        