/* Write your T-SQL query statement below */
select max(salary)  as SecondHighestSalary 
from(
    select salary , rank() over(order by salary desc) as ranksal
     from  Employee )  as r
where ranksal >1