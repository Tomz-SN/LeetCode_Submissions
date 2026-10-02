class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pack = s.split()
        return len(pack[len(pack)-1])
        