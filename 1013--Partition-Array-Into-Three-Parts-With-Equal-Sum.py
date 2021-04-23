"""
Time Limit Exceeded
"""
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        length = len(arr)
        for mid_one in range(1,length):
            for mid_two in range(mid_one +1 ,length):
                if sum(arr[:mid_one]) == sum(arr[mid_one:mid_two]) == sum(arr[mid_two:]):
                    return True
        return False
        
"""
Runtime: 296 ms, faster than 92.78% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
Memory Usage: 21.1 MB, less than 59.75% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
"""
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total%3 != 0 : 
            return False
        cumsum = 0
        count = 0
        summation = total//3
        for num in arr:
            cumsum += num
            if summation == cumsum :
                count+=1
                cumsum=0
        return count>=3
