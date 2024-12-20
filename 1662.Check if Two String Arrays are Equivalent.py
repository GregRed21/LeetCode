class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        # str1 = ''
        # str2 = ''
        # for i in word1:
        #     str1+=i
        # for i in word2:
        #     str2+=i
        # if str1 == str2:
        #     return True
        # else:
        #     return False
        return ''.join(word1) == ''.join(word2)
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(Solution().arrayStringsAreEqual(word1, word2))