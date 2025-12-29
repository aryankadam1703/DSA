# Write your MySQL query statement below
select r.contest_id,
round((count(contest_id)/(select count(user_id) from users))*100,2) as percentage from Users u 
right join register r
on u.user_id = r.user_id
group by r.contest_id
order by percentage desc,contest_id asc