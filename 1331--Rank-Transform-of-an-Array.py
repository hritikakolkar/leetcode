"""
Runtime: 356 ms, faster than 43.67% of Python3 online submissions for Rank Transform of an Array.
Memory Usage: 31.7 MB, less than 81.00% of Python3 online submissions for Rank Transform of an Array.
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        sorted_arr = sorted(arr)
        dictionary = {sorted_arr[0]:1}
        rank=1
        for idx in range(1,len(sorted_arr)) :
            if sorted_arr[idx] != sorted_arr[idx-1] :
                rank += 1
                dictionary[sorted_arr[idx]] = rank
        ans = list()
        for num in arr :
            ans.append(dictionary[num])
        return ans
      
"""
Runtime: 344 ms, faster than 69.98% of Python3 online submissions for Rank Transform of an Array.
Memory Usage: 33.4 MB, less than 53.17% of Python3 online submissions for Rank Transform of an Array.
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        Ranking = dict(zip( sorted(set(arr)), range(1,len(arr)+1)))
        for idx in range(len(arr)):
            arr[idx] = Ranking[arr[idx]]
        return arr
      
"""
Runtime: 348 ms, faster than 61.03% of Python3 online submissions for Rank Transform of an Array.
Memory Usage: 34.7 MB, less than 33.08% of Python3 online submissions for Rank Transform of an Array.
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return list(map({element:rank for rank, element in enumerate(sorted(set(arr)),start = 1)}.get, arr))
      
"""
Runtime: 344 ms, faster than 69.98% of Python3 online submissions for Rank Transform of an Array.
Memory Usage: 31.7 MB, less than 81.00% of Python3 online submissions for Rank Transform of an Array.
"""
class Solution:
	def arrayRankTransform(self, arr: List[int]) -> List[int]:
		rank,dictionary,prev = 0,{},None
		for num in sorted(arr):
			if prev != num:
				prev = num
				rank += 1
				dictionary[prev] = rank
		return [dictionary[num] for num in arr ]
