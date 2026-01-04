# Write your MySQL query statement below

with highest_user_rating as(
    select u.name,count(m.user_id) as Total_count from Movierating m
    left join users u
    on m.user_id = u.user_id
    group by m.user_id,u.name
),
user_rated_more as(
    select name from highest_user_rating 
    order by Total_count desc, name asc
    limit 1
),

highest_movie_rated as(
    select m1.title,avg(m.rating) as avg_rating from movies m1
    right join movierating m
    on m1.movie_id = m.movie_id
    where m.created_at >='2020-02-01' and m.created_at < '2020-03-01'
    group by m1.title
),
max_avg_movie as(
    select title from highest_movie_rated
    order by avg_rating desc,title asc
    limit 1
),
output as(
    select * from user_rated_more
    union all
    select * from max_avg_movie
)
select name as results from output




    
