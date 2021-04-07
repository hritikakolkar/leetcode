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

# Solution After 11 months
class Solution1:
    def sumZero(self, n: int) -> List[int]:
        ans = list()
        if not n & 1:
            for i in range(1,n//2+1):
                ans.append(i)
                ans.append(-1*i)
        else:
            ans.append(0)
            for i in range(1,n//2+1):
                ans.append(i)
                ans.append(-1*i)
        return ans
                
class Solution2:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1,n))+[int(-1*n*(n-1)*0.5)]

