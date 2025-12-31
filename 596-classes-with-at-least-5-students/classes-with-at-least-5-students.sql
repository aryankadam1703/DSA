# Write your MySQL query statement below
with Limit_Class as (
    select class from Courses
    group by class
    having count(student) >=5
)
select * from Limit_Class;