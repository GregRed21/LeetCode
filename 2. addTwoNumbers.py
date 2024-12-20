class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)  # Временный узел для упрощения кода
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # Суммируем значения и перенос
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            # Переходим к следующему узлу
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy_head.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]

print(Solution().addTwoNumbers(l1, l2))

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         # print(l1)
#         # print(l2)
#         # print(type(l1))
#         # print(type(l2))
#         a = ''
#         b = ''
#         for i in l1[::-1]:
#             a += str(i)
#         for i in l2[::-1]:
#             b += str(i)
#         final_list = int(a) + int(b)
#         final_list = str(final_list)
#         list(final_list)
#         final_list = final_list[::-1]
#         return list(final_list)
#
# l3 = [2, 4, 3]
# l4 = [5, 6, 4]
#
# print(Solution().addTwoNumbers(l3, l4))
#
# print(l3)
# print(l4)
# print(type(l3))
# print(type(l4))
