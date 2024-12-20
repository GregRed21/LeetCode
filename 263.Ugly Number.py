class Solution:
    def isUgly(self, n):
        if n<1:
            return False

        for factor in(2,3,5):
            while n%factor==0:
                n//=factor

        return n==1
n = 48
print(Solution().isUgly(n))