/* Write your T-SQL query statement below */
select employee_id  from Employees
where employee_id not in 
( select e.employee_id 
from Employees as e   join Salaries as s
on e.employee_id = s.employee_id
)
union 
select employee_id  from Salaries 
where employee_id not in 
( select e.employee_id 
from Employees as e   join Salaries as s
on e.employee_id = s.employee_id
)
