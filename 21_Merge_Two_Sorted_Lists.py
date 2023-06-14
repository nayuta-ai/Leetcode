from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self,
                 val: int = 0,
                 next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class MergeTwoLists:
    def merge_two_lists(
            self,
            list1: Optional[ListNode],
            list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or list2 and list2.val < list1.val:
            list1, list2 = list2, list1
        if list1:
            list1.next = self.merge_two_lists(list1.next, list2)
        return list1
