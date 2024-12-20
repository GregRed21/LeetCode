from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        pre, cur = head, head.next

        while cur != None:
            while cur != None and cur.val == pre.val:
                cur = cur.next
            pre.next = cur
            pre = cur
            if cur != None:
                cur = cur.next

        return head