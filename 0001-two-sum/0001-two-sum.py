class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table = {}
        for index,num in enumerate(nums):
            sub = target-num
            if sub in table:
                return [table[sub],index]
            else:
                table[num] = index

        
        