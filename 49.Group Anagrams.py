class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for word in strs:
            counts = [0]*26
            for char in word:
                counts[ord(char)-ord("a")]+=1
            key = tuple(counts)
            if key not in result:
                result[key]=[]
            result[key].append(word)
        return list(result.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))