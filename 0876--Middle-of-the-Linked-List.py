"""
Runtime: 32 ms, faster than 45.39% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.2 MB, less than 41.71% of Python3 online submissions for Middle of the Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slowNode = fastNode = head
        while fastNode and fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        return slowNode
