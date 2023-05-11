from collections import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.traverseDFS(head, root)

    def traverseDFS(self, head, treeNode):
        if not treeNode:
            return False

        ret = self.checkDFS(head, treeNode)
        if ret:
            return ret

        return self.traverseDFS(head, treeNode.left) or self.traverseDFS(head, treeNode.right)

    def checkDFS(self, listNode, treeNode):
        if listNode == None:
            return True

        elif treeNode == None:
            return False

        elif treeNode.val == listNode.val:
            return self.checkDFS(listNode.next, treeNode.left) or self.checkDFS(listNode.next, treeNode.right)

        return False