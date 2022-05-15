/* Write your T-SQL query statement below */
select user_id , CONCAT (upper(left(name ,1)) , lower(SUBSTRING(name , 2, len(name) ))  )as name
from Users
order by user_id ;