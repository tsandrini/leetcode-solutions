from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        out_head = ListNode()
        carry = 0
        curr = out_head
        while (l1 != None) or (l2 != None) or (carry != 0):
            _sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = _sum // 10
            curr.next = ListNode(_sum % 10)
            curr = curr.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return out_head.next
