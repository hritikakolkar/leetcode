"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        lst=[]
        if n%2==0:
            for i in range(n+1):
                if not  i==n//2:
                    lst.append(n//2-i)
        else:
            for i in range(n):
                lst.append(n//2-i)
        return lst
