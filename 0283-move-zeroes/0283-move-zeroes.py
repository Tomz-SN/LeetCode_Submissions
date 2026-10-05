class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        count = 0
        for n in nums:
            if n == 0:
                count +=1
        for i in range (count):
            nums.remove(0)
        for i in range (count):
            nums.append(0)

        