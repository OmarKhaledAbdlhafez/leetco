/* Write your T-SQL query statement below */
update Salary
set sex = case when sex = 'f' then 'm'
when sex = 'm' then 'f'
end 

select id  , name , sex
,salary  
from Salary
order by id