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
