"""
888. Fair Candy Swap

Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.
"""
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A_B=sum(A)-sum(B)
        """
        for candy_lenA in A:
            for candy_lenB in B:
                if sum_A-candy_lenA+candy_lenB==sum_B-candy_lenB+candy_lenA:
                    return [candy_lenA,candy_lenB]
        """
        set_B=set(B)
        for candy_lenA in A:
            val=int(candy_lenA-(sum_A_B)/2)
            if val in set_B:
                return [candy_lenA,val]

# After 11 months solution
# Time Limit Exceeded
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        s = sum(A) -  sum(B)
        for i in range(len(A)):
            for j in range(len(B)):
                if s - 2*A[i] + 2*B[j] == 0 :
                    return [A[i],B[j]]
                  
"""
Runtime: 3044 ms, faster than 22.16% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 16.3 MB, less than 76.53% of Python3 online submissions for Fair Candy Swap.
"""
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        s = int((sum(B) -  sum(A))/2)
        for c_A in A:
            if c_A + s in B:
                return [c_A, c_A + s]
            
"""
Runtime: 4972 ms, faster than 13.04% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 17.3 MB, less than 16.17% of Python3 online submissions for Fair Candy Swap.
"""
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        s = int((sum(B) -  sum(A))/2)
        for c_A in set(A):
            if c_A + s in set(B):
                return [c_A, c_A + s]
"""
Runtime: 356 ms, faster than 72.10% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 17.4 MB, less than 7.17% of Python3 online submissions for Fair Candy Swap.
"""
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        s = int((sum(B) -  sum(A))/2)
        setA, setB = set(A), set(B)
        for c_A in setA:
            if c_A + s in setB:
                return [c_A, c_A + s]
              
"""
Runtime: 360 ms, faster than 63.36% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 16.8 MB, less than 35.59% of Python3 online submissions for Fair Candy Swap.
"""
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        s = int((sum(B) -  sum(A))/2)
        setB = set(B)
        for c_A in A:
            if c_A + s in setB:
                return [c_A, c_A + s]
