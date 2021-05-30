"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for customer_account in accounts:
            wealth = sum(customer_account)
            max_wealth = max(wealth,max_wealth) 
        return max_wealth
    
