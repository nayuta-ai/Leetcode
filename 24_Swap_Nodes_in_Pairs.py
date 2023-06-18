from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = node = ListNode(0)
        res.next = head
        while head and head.next:
            prev = head.next
            head.next = prev.next
            prev.next = head
            node.next = prev
            node = prev.next
            head = head.next
        return res.next