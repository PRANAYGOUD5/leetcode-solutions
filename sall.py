class Solution:
    def average(self, salary: List[int]) -> float:
        c=0
        mn=min(salary)
        mx=max(salary)
        salary.remove(mn)
        salary.remove(mx)
        n=len(salary)
        su=sum(salary)
        return su/n
            
