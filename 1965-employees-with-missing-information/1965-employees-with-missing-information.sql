/* Write your T-SQL query statement below */
/*select employee_id  from Employees
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
)*/

select isnull(e.employee_id, s.employee_id ) as employee_id
from Employees as e full outer  join Salaries as s
on e.employee_id = s.employee_id
where name is null or salary is null 
order by employee_id
