class Solution:
    def hammingWeight(self, n: int) -> int:
        return (0 * n.bit_count() | n).bit_count()