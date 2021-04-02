class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        if n==1: return prices
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]<=prices[i]:
                    prices[i]-=prices[j]
                    break
        return prices

class Solution1:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            while stack and (prices[stack[-1]] >= prices[i]):
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices
