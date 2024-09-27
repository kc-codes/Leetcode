class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
       
        
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] +1
            else:
                d[i] = 1 

        
        # freq = Counter(nums)
        
        for count in d.values():
            if count > 2:
                return False
        
        
        unique_elements = len(d)
        return unique_elements >= len(nums) // 2



        # freq = Counter(nums)
        
        # for count in freq.values():
        #     if count > 2:
        #         return False
        
        
        # unique_elements = len(freq)
        # return unique_elements >= len(nums) // 2