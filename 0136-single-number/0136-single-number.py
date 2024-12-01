class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Using XOR

        res = 0
        for n in nums:
            res = n ^ res
        return res
        