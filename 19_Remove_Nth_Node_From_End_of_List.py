from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         p = head
#         length = 0
#         while p:
#             length += 1
#             p = p.next
#         node = ListNode(0)
#         node.next = head
#         curr = node
#         n = length - n + 1
#         while n > 1:
#             curr = curr.next
#             n -= 1
#         if curr.next.next:
#             curr.next = curr.next.next
#         else:
#             curr.next = None

#         return node.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head