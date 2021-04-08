# Not a good Solution
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        one_places=[i for i in range(len(nums)) if nums[i]==1]
        places_away=[one_places[i]-one_places[i-1]-1 for i in range(1,len(one_places))]
        for away in places_away:
            if away<k:
                return False
        return True
 
class Solution1:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = -1
        for i in range(len(nums)):
            if nums[i]==1:
                if idx != -1 and i-idx-1<k:
                    return False
                idx = i
        return True
 
class Solution2:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count_0=k
        for num in nums:
            if num == 1:
                if count_0<k:
                    return False
                count_0=0
            else:
                count_0+=1
        return True
