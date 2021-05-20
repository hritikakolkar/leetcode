"""
Runtime: 48 ms, faster than 8.74% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.1 MB, less than 82.85% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None :
            return head
        currentNode = head
        while currentNode.next :
            if currentNode.val == currentNode.next.val :
                currentNode.next = currentNode.next.next
            else :
                currentNode = currentNode.next
        return head

"""
Runtime: 44 ms, faster than 48.77% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14 MB, less than 94.76% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head :
            return head
        slowNode = head
        fastNode = head.next
        while fastNode :
            if slowNode.val != fastNode.val :
                slowNode.next = fastNode
                slowNode = fastNode
            fastNode = fastNode.next
        if slowNode.next and slowNode.val == slowNode.next.val :
            slowNode.next = None
        return head
