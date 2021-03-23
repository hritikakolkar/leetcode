"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i=0
        xor=0
        while i<n:
            xor=xor^(start + 2*i)
            i+=1
        return xor
