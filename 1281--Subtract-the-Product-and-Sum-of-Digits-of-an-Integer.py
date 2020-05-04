#1281. Subtract the Product and Sum of Digits of an Intege
#Given an integer number n, return the difference between the product of its digits and the sum of its digits.
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_n=1
        sum_n=0
        while n>0:
            product_n*=n%10
            sum_n+=n%10
        return product_n-sum_n
            
