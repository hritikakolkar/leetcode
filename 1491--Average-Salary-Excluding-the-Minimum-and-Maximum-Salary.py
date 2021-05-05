"""
Runtime: 32 ms, faster than 54.66% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
Memory Usage: 14.3 MB, less than 7.81% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        """
        min_salary=1000000
        max_salary=0
        summation=0
        for sal in salary:
            if sal<min_salary:
                min_salary = sal
            if sal>max_salary:
                max_salary = sal
            summation += sal
        return (summation - max_salary - min_salary)/(len(salary)-2)
        """
        salary.sort()
        return sum(salary[1:-1])/(len(salary)-2)
