# Write your MySQL query statement below

-- SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
-- FROM Employee e
-- JOIN Department d 
-- ON e.departmentId = d.id
-- WHERE(
--     SELECT COUNT(DISTINCT e2.salary)
--     FROM Employee e2
--     WHERE e2.departmentId = e.departmentId AND e2.salary >= e.salary
-- ) <= 3
-- ORDER BY
-- d.name, e.salary DESC;


with highest_earner as(
    select d.name as Department,e.name as Employee,e.salary as Salary,
    dense_rank() over (partition by d.name order by e.salary desc) as rnk
    from Employee e
    left join Department d
    on e.departmentId=d.id    
)
select Department,Employee,Salary from highest_earner
where rnk<=3;







