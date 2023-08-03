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
