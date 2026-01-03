# Write your MySQL query statement below
with low as(
    select * from Accounts
    where income<20000
),
average as(
    select * from Accounts
    where income >= 20000 and income<=50000
),
high as(
    select * from Accounts
    where income > 50000
)

select 'Low Salary' as category,count(*) as accounts_count
from low
union
select 'Average Salary' as category,count(*) as accounts_count
from average
union
select 'High Salary' as category,count(*) as accounts_count
from high