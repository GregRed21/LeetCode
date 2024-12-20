import math
# print(int(math.sqrt(144)))
class Solution:
    def judgeSquareSum(self, c):
        # list_n = []
        # for i in range(0, int(math.sqrt(c)+1)):
        #     list_n.append(i)
        # # print(list_n)
        # for i in list_n:
        #     for j in list_n:
        #         # print(i**2+j**2)
        #         if (i**2+j**2)==c:
        #             return True
        #     continue
        # return False

        left = 0
        right = int(math.sqrt(c))

        while left<=right:
            total = left**2+right**2
            if total == c:
                return True

            if total >c:
                right-=1
            else:
                left+=1
        return False


c = 999999999
print(Solution().judgeSquareSum(c))