class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = list()
        for idx in range(n) :
            ans.extend([nums[idx],nums[idx+n]])
        return ans
