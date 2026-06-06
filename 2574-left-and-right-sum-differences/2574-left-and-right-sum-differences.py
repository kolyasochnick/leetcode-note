class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        leftPref = [0] * n
        rightPref = [0] * n

        for i in range(n):
            leftPref[i] = leftPref[i - 1] + nums[i]
            rightPref[~i] = rightPref[~i + 1] + nums[~i]
        
        res = []
        for i in range(n):
            if i < n - 1:
                rightSum = rightPref[i + 1]
            else:
                rightSum = 0
            if i > 0:
                leftSum = leftPref[i - 1]
            else:
                leftSum = 0
            res.append(abs(leftSum - rightSum))

        return res
            



        return []
        