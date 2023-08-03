# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Stack based Solution
# 553ms Beats 96.71% of users with Python3
# 49.21mb Beats 29.08% of users with Python3
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        halfPtr = lastPtr = head
        if lastPtr.next == None:
            return True
        while lastPtr and lastPtr.next:
            stack.append(halfPtr.val)
            halfPtr = halfPtr.next
            lastPtr = lastPtr.next.next
        if lastPtr != None:
            halfPtr = halfPtr.next
        while halfPtr:
            if stack.pop() != halfPtr.val:
                return False
            halfPtr = halfPtr.next 
        return True

# O(n) time and O(1) space Solution, Reversing half of the list
# 482ms Beats 99.75%of users with Python3
# 33.53mb Beats 96.21%of users with Python3
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        halfPtr = head
        lastPtr = head
        prevPtr = None
        if head.next == None:
            return True

        while lastPtr and lastPtr.next:
            lastPtr = lastPtr.next.next

            tmpPtr = halfPtr.next
            halfPtr.next = prevPtr
            prevPtr = halfPtr
            halfPtr = tmpPtr

        if lastPtr != None:
            halfPtr = halfPtr.next
        
        while halfPtr and prevPtr:
            if halfPtr.val != prevPtr.val:
                return False
            halfPtr = halfPtr.next
            prevPtr = prevPtr.next
        return True
