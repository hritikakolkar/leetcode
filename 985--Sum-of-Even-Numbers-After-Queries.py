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
