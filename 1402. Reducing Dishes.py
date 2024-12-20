class Solution:
    def maxSatisfaction(self, satisfaction):
        mainList = sorted(satisfaction, reverse=True)
        Total = []
        goodEda = 0
        print(mainList)
        for item in mainList:
            goodEda+=item
            if goodEda>0:
                Total.append(item)
            else:
                break
        max_Total = sorted(Total)
        q = 0
        e = 1
        norm_Tot = []
        while q<len(max_Total):
            norm_Tot.append(max_Total[q]*e)
            q+=1
            e+=1
        print(norm_Tot)
        print(sum(norm_Tot))


# satisfaction = [-1, -8, 0, 5, -9]
# satisfaction = [-1, -4, -5]
satisfaction = [-2,5,-1,0,3,-3]

Solution().maxSatisfaction(satisfaction)

# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         total = 0
#         satisfaction_total = 0
#         for s in sorted(satisfaction, reverse=True):
#             satisfaction_total += s
#             if satisfaction_total<=0:
#                 return total
#             total += satisfaction_total
#         return total