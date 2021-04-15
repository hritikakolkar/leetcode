# Time Limit Exceeded
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        answer=[]
        for i in range(len(A)):
            val = queries[i][0]
            index = queries[i][1]
            A[index]+=val
            summation = 0
            for i in A:
                if not i & 1:
                    summation+=i
            answer.append(summation)
        return answer

"""
Runtime: 492 ms, faster than 96.51% of Python3 online submissions for Sum of Even Numbers After Queries.
Memory Usage: 20.1 MB, less than 95.85% of Python3 online submissions for Sum of Even Numbers After Queries.
"""
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        summation = sum(num for num in A if not num & 1)
        for val,index in queries :
            if A[index]%2 == 0:
                summation -= A[index]
            A[index] += val
            if A[index]%2==0:
                summation += A[index]
            ans.append(summation)
        return ans
