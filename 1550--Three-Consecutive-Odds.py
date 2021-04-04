class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        length=len(arr)
        if length<3:
            return False
        for i in range(2,length):
            if arr[i]%2==1 and arr[i-1]%2==1 and arr[i-2]%2==1:
                return True
        return False
 
 #Found Good Solution 99% space complexities
 class Solution1:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        for num in arr:
            if num%2==1:
                count+=1
            else:
                count=0
            if count==3:
                return True
        return False

#Good with both complexities
class Solution2:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        for num in arr:
            if num & 1:
                count+=1
                if count==3:
                    return True
            else:
                count=0

        return False
            
