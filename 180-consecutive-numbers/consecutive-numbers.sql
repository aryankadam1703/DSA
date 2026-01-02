# Write your MySQL query statement below

-- SELECT DISTINCT l1.num AS ConsecutiveNums
-- FROM Logs l1 
-- join Logs l2
-- join Logs l3
-- WHERE l1.num = l2.num
--   AND l2.num = l3.num
--   AND l1.id = l2.id - 1
--   AND l2.id = l3.id - 1;

-- with cte as (
--     select num,
--     lead(num,1) over() num1,
--     lead(num,2) over() num2
--     from logs

-- )
-- select distinct num ConsecutiveNums from cte where (num=num1) and (num=num2)

SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1 
join Logs l2
on l1.id = l2.id+1
join Logs l3
on l1.id = l3.id+2
WHERE l1.num = l2.num AND l2.num = l3.num