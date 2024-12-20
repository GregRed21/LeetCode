# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2=list2.next

            tail = tail.next

        tail.next = list1 or list2

        return dummy.next
        # result = None
        # if result is None:
        #     result = ListNode()
