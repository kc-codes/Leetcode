class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
       
        freq = Counter(nums)
        
        
        for count in freq.values():
            if count > 2:
                return False
        
        
        unique_elements = len(freq)
        return unique_elements >= len(nums) // 2