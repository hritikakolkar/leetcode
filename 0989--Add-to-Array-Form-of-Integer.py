"""
Runtime: 268 ms, faster than 93.68% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15.1 MB, less than 59.74% of Python3 online submissions for Add to Array-Form of Integer.
"""
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for idx in range(len(num)-1, -1, -1) :
            k, num[idx] = divmod(k+num[idx], 10)
        if k :
            ans = list(map(int, str(k)))
            ans.extend(num)
        else :
            ans = num
        del num
        return ans

"""
Runtime: 280 ms, faster than 87.82% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15 MB, less than 87.25% of Python3 online submissions for Add to Array-Form of Integer.
"""
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for idx in range(len(num)-1, -1, -1) :
            k, num[idx] = divmod(k+num[idx], 10)
        if k :
            num = list(map(int,str(k))) + num
        return num
