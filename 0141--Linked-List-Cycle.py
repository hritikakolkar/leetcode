"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# brute force approach
# 59ms Beats 94.84%of users with Python3
# 20.69mb Beats 27.96%of users with Python3

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            hashTable = {}
            currentNode = head
            while currentNode:
                if hashTable.get(currentNode, False):
                    return True
                hashTable[currentNode] = True
                currentNode = currentNode.next
            return False
        else:
            return False

# two pointer approach
# 59ms Beats 94.84%of users with Python3
# 20.21mb Beats 87.57%of users with Python3
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            slowPtr = head
            fastPtr = head.next.next
            while slowPtr != fastPtr:
                if not (slowPtr and fastPtr and fastPtr.next):
                    return False
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next.next
            return True
        else:
            return False

# tmp method
# 49ms Beats 99.37%of users with Python3
# 18.48mb Beats 99.60%of users with Python3
"""
Create a "visited" node (value is infinity, next pointer is None)
Every time we visit a node, we replace it with that value and next pointer
If we visit such a node in the future, that means there must be a cycle!    
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp = ListNode()
        currentNode = head
        while currentNode:
            if currentNode == tmp:
                return True
            nextNode = currentNode.next
            currentNode.next = tmp
            currentNode = nextNode
        return False
