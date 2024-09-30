class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        print(ans)


        for i in nums:
            ans.append(i)
        for i in nums:
            ans.append(i)
        return ans

        #Method 2:
        # return nums * 2

        # Method 3:        
        # return nums + nums

        # Method 4:        
        # nums.extend(nums)  # Extend the list with itself
        # return nums

        # Method 5:
        # n = len(nums)
        # result = [0] * (2 * n)  # Create a new list of size 2n
        # for i in range(n):
        #     result[i] = nums[i]      # Copy the first part
        #     result[i + n] = nums[i]  # Copy the second part
        # return result