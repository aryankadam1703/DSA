# Write your MySQL query statement below
select C.name from Customer C
left join Customer R
on C.referee_id = R.id
where C.referee_id !=2 or C.referee_id is null;
