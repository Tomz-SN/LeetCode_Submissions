class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(len(nums1)-m):
            nums1.remove(0)
        for j in range(len(nums2)-n):
            nums2.remove(0)
        for num in nums2:
            nums1.append(num)
        nums1.sort()