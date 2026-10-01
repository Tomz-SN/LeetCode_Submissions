class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSum = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i,-1,-1):
                sum += nums[j]
            runningSum.append(sum)
        return runningSum