class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.rstrip()
        count = 0
        for i in a[::-1]:
            if i == ' ':
                break
            else:
                count+=1
        return count


s = "luffy is still joyboy"
print(Solution().lengthOfLastWord(s))