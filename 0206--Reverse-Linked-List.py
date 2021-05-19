"""
Runtime: 36 ms, faster than 61.81% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.7 MB, less than 42.23% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None :
            return head
        currentNode = head
        nextNode = head.next
        currentNode.next = None
        while nextNode :
            print(currentNode.val)
            tmp = nextNode.next
            nextNode.next = currentNode
            currentNode = nextNode
            nextNode = tmp
        return currentNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None :
            return head
        currentNode = head
        nextNode = head.next
        currentNode.next = None
        while nextNode :
            print(currentNode.val)
            tmp = nextNode.next
            nextNode.next = currentNode
            currentNode = nextNode
            nextNode = tmp
        return currentNode
        
"""
Runtime: 28 ms, faster than 95.89% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.5 MB, less than 74.75% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        currentNode = head
        previousNode = None
        while currentNode :
            tmpNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = tmpNode
        return previousNode
