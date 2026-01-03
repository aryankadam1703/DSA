# Write your MySQL query statement below
with Total as(
    select person_name,
    sum(weight) over (order by turn) as Total_Weight
    from Queue
)
select person_name from Total
where Total_Weight <=1000
order by Total_Weight desc
limit 1