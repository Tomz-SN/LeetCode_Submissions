class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for n in nums:
            if n >= target:
                return nums.index(n)
        return nums.index(n)+1
        