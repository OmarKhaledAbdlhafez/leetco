/* Write your T-SQL query statement below */
with graph as 
(
 select t1.id as id , t1.p_id as p1 , t2.p_id  as p2
 from Tree as t1  left join Tree as t2 
 on t1.id = t2.p_id
)

select distinct id , 
case 
when p1 is null then 'Root'
when p2 is  null  then 'Leaf'
else 'Inner' 
end as type
from graph
order by id 