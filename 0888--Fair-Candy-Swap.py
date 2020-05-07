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
