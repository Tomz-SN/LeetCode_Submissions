class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSum = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            runningSum.append(sum)
        return runningSum