class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)
# haystack = "leetcode"
# needle = "leeto"
haystack = "sadbutsad"
needle = "sad"
print(Solution().strStr(haystack, needle))