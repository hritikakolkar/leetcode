"""
Runtime: 36 ms, faster than 84.71% of Python3 online submissions for Defuse the Bomb.
Memory Usage: 14.3 MB, less than 34.43% of Python3 online submissions for Defuse the Bomb.
"""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length=len(code)
        if k>0:
            code=code+code
            for i in range(length):
                code[i]=sum(code[i+1:i+k+1])
            return code[:length]
        elif k==0:
            return [0]*length
        else:
            code=code+code
            for i in range(length,2*length):
                code[i-length]=sum(code[i+k:i])
            return code[:length]
          
"""
Runtime: 32 ms, faster than 94.57% of Python3 online submissions for Defuse the Bomb.
Memory Usage: 14.1 MB, less than 83.14% of Python3 online submissions for Defuse the Bomb.
"""
class Solution1:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length=len(code)
        if k==0: return [0]*length
        code = code*2
        for i in range(length):
            if k>0:
                code[i] = sum(code[i+1:i+k+1])
            else:
                code[i] = sum(code[i+length+k:i+length])
        return code[:length]
