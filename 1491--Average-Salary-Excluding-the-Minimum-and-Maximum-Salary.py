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
