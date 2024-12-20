from typing import List


class Solution:
    def plusOne(self, digits: List[int])->List[int]:
        str_dig = ''
        for i in digits:
            str_dig+=str(i)
        str_dig = int(str_dig)
        str_dig+=1
        str_dig = str(str_dig)
        list_dig = []
        for i in str_dig:
            list_dig.append(int(i))
        return list_dig
digits = [1,2,3]

print(Solution().plusOne(digits))
