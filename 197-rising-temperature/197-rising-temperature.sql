/* Write your T-SQL query statement below */
/*
with t as (
select id ,
    DATEDIFF (day ,lag (recordDate ,1) over (order by id ),recordDate ) as days
    ,( temperature - lag (temperature ,1) over (order by id )) as diff
    from Weather 
    /*order by recordDate*/
)

select id 
from  t
where diff >0 and days = 1  */

with temp as(
select w1.id as id, w1.recordDate, w1.temperature as today, w2.temperature as yesterday
from Weather w1
join Weather w2
on dateadd(d,1,w2.recordDate) = w1.recordDate
)
select id
from temp
where today > yesterday