class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        print(strx)
        listx = list(strx)
        print(listx)
        if listx == listx[::-1]:
            return True
        else:
            return False

x = 121

print(Solution().isPalindrome(x))

