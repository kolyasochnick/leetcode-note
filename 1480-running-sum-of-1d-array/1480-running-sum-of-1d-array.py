class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0] * len(nums)
        for i in range(len(nums)):
            runningSum[i] = runningSum[i-1] + nums[i] 
        return runningSum