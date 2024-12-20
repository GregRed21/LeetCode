class Solution:
    def containsDuplicate(self, nums):
        known = set()
        for num in nums:
            if num in known:
                print(known)
                return True
            known.add(num)
        return False

nums = [1,1,1,3,3,4,3,2,4,2]

print(Solution().containsDuplicate(nums))



# class Solution:
#     def containsDuplicate(self, nums):
#         list_set = set(nums)
#         list_set = list(list_set)
#         if len(nums)>len(list_set):
#             return True
#         else:
#             return False
# nums = [1,1,1,3,3,4,3,2,4,2]
# # nums = [1,2,3,1]
# # nums = [1,2,3]
# print(Solution().containsDuplicate(nums))