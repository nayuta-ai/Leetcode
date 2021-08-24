# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# time O(m+n) m:length of headA, n:length of headB
# space O(m+n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p, q = headA, headB 
        while p != q :
            if not p:
                p = headB
            else:
                p = p.next
            if not q:
                q = headA
            else:
                q = q.next
        return p