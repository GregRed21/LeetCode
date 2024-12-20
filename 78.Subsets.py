from itertools import combinations
class Solution:
    def subsets(self, nums):
        result = [[]]
        for i in range(1, len(nums)+1):
            result.extend(combinations(nums, i))
        return result
nums = [1,2,3]
print(Solution().subsets(nums))