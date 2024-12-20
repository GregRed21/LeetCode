# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
# Example 4:
# Input: s = "([])"
# Output: true






# class Solution:
#     def isValid(self, s: str) -> bool:
#         s = list(s)
#         Norm = ['(', ')','[', ']','{','}']
#         count = 0
#         listTrue = []
#         while count < len(s):
#             if Norm[count] in s and Norm[count+1] in s and s.index(Norm[count])<s.index(Norm[count+1]):
#                 # if (Norm[2] in s and Norm[3] in s) and s.index(Norm[2]) < s.index(Norm[1]) and s.index(Norm[3]) > s.index(Norm[1]):
#                 #     listTrue.append('False')
#                 # else:
#                 #     pass
#                 listTrue.append('True')
#             else:
#                 listTrue.append('False')
#             count+=2
#
#         print(listTrue)
#         if all(i == 'True' for i in listTrue):
#             return True
#         else:
#             return False
#
# s = "[([()][()])]"
#
# print(Solution().isValid(s))


class Solution:
    def isValid(self, s: str) -> bool:
        listTrue = []
        if s!='':
            if '(' in s and ')' in s:
                if s.index('(')<s.index(')'):
                    listTrue.append('True')
                else:
                    listTrue.append('False')
                if s.count('(')==s.count(')'):
                    listTrue.append('True')
                else:
                    listTrue.append('False')
                listTrue.append('True')
            else:
                pass
            if s.count('(')!=s.count(')'):
                listTrue.append('False')
            else:
                pass
            if '[' in s and ']' in s:
                if s.index('[') < s.index(']'):
                    listTrue.append('True')
                else:
                    listTrue.append('False')
                if s.count('[') == s.count(']'):
                    listTrue.append('True')
                else:
                    listTrue.append('False')
                listTrue.append('True')
            else:
                pass
            if s.count('[')!=s.count(']'):
                listTrue.append('False')
            else:
                pass
            if '{' in s and '}' in s:
                if s.index('{') < s.index('}'):
                    listTrue.append('True')
                else:
                    listTrue.append('False')
                if s.count('{') == s.count('}'):
                    listTrue.append('True')
                else:
                    listTrue.append('False')
                listTrue.append('True')
            else:
                pass
            if s.count('{')!=s.count('}'):
                listTrue.append('False')
            else:
                pass
            if '([)' in s or '(])' in s or '({)' in s or '(})' in s or '([]]' in s:
                listTrue.append('False')
            else:
                pass
            if '[(]' in s or '[)]' in s or '[{]' in s or '[}]' in s or '{]' in s:
                listTrue.append('False')
            else:
                pass
            if '{(}' in s or '{)}' in s or '{[}' in s or '{]}' in s or '{}}{' in s:
                listTrue.append('False')
            else:
                pass
        else:
            listTrue.append('False')
        print(listTrue)
        if listTrue == []:
            return False
        else:
            pass
        if all(i == 'True' for i in listTrue):
            return True
        else:
            return False

s = "[([]])"

print(Solution().isValid(s))