# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(nums):
#             for j in range i:

#                 if :
#                     return True
#                 else:
#                     return False




# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(nums):
#             if nums[0]==nums[1]:
#                 return True
#             else:
#                 return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
