class Solution:
    def removeElement(self, nums, val):
        q = 0
        while q<len(nums):
            if nums[q]==val:
                nums.remove(nums[q])
                continue
            q+=1
        k = len(nums)
        return k

nums = [0,1,2,2,3,0,4,2]
val = 2

print(Solution().removeElement(nums, val))