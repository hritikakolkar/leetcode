"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 """

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even,odd=[],[]
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        return even+odd
#new solution using two pointers
class Solution1:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        def even(num):
            if num%2==0:
                return True
            return False
        front=0
        back=len(A)-1
        while front<back:
            if even(A[back]) and (not even(A[front])):
                A[back],A[front]=A[front],A[back]
                front+=1
                back-=1
            elif even(A[front]):
                front+=1
            elif not even(A[back]):
                back-=1
        return A
 
#After 11 months solution
class Solution2:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i=0
        j=len(A)-1
        while i<j:
            if A[i]%2>A[j]%2:
                A[i],A[j]=A[j],A[i]
            if A[i]%2==0:
                i+=1
            if A[j]%2==1:
                j-=1
        return A
                
