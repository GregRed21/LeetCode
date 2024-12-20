from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        for i in nums:
            if i<target:
                count+=1

        return count

nums = [1,3,5,6]
target = 5

print(Solution().searchInsert(nums, target))