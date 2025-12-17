# Write your MySQL query statement below
select distinct A.author_id as id from Views A
where viewer_id = author_id
order by id
