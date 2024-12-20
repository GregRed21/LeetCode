class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs[0] == strs[0].lower() and len(strs)!=0:
            res = ''
            strs = sorted(strs)
            for i in strs[0]:
                if strs[-1].startswith(res+i):
                    res+=i
                else:
                    break
            return res
        else:
            return ''

strs = ["flower","flow","flight"]

print(Solution().longestCommonPrefix(strs))