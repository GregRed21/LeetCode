class Solution:
    def maxDistance(self, arrays):
        num_min = 10000
        num_max = -10000
        res = 0
        for i in arrays:
            res = max(res, i[-1] - num_min, num_max - i[0])
            num_min = min(num_min, i[0])
            num_max = max(num_max, i[-1])
        return res
arrays = [[1,4],[0,5]]
print(Solution().maxDistance(arrays))