class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)
     
class Solution1:
    def fib(self, n: int) -> int:
        memory={0:0,1:1}
        if n in memory:
            return memory[n]
        else:
            memory[n]=self.fib(n-1) + self.fib(n-2)
            return memory[n]
 
#99% time 
class Solution2:
    def fib(self, N: int) -> int:
        self.cache = {0: 0, 1: 1}
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        if N in self.cache.keys():
            return self.cache[N]
        self.cache[N] = self.memoize(N-1) + self.memoize(N-2)
        return self.memoize(N)
      
