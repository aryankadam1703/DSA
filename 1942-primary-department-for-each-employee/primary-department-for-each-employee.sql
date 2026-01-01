# Write your MySQL query statement below
with Single_Dept_Emp as(
    select employee_id,department_id,count(department_id) as cnt  from Employee
    group by employee_id
    having cnt = 1
)

select employee_id,department_id from Single_Dept_Emp
union
select employee_id,department_id from Employee
where primary_flag = 'Y'
 