from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        out_head = ListNode()

        buff1: Optional[ListNode] = l1
        buff2: Optional[ListNode] = l2
        carry: int = 0
        _sum: int = 0
        prev: ListNode = out_head
        curr: ListNode
        while (buff1 != None) or (buff2 != None):
            _sum = (
                (buff1.val if buff1 is not None else 0)
                + (buff2.val if buff2 is not None else 0)
                + carry
            )
            curr = ListNode(_sum % 10)
            carry = _sum // 10

            prev.next = curr
            prev = curr

            if buff1 is not None:
                buff1 = buff1.next
            if buff2 is not None:
                buff2 = buff2.next

        if carry != 0:
            prev.next = ListNode(carry)

        return out_head.next if out_head.next != None else out_head


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        out_head = ListNode()

        buff1: Optional[ListNode] = l1
        buff2: Optional[ListNode] = l2
        carry: int = 0
        _sum: int = 0
        prev: ListNode = out_head
        curr: ListNode
        while (buff1 != None) or (buff2 != None):
            _sum = (
                (buff1.val if buff1 is not None else 0)
                + (buff2.val if buff2 is not None else 0)
                + carry
            )
            curr = ListNode(_sum % 10)
            carry = _sum // 10

            prev.next = curr
            prev = curr

            if buff1 is not None:
                buff1 = buff1.next
            if buff2 is not None:
                buff2 = buff2.next

        if carry != 0:
            prev.next = ListNode(carry)

        return out_head.next if out_head.next != None else out_head
