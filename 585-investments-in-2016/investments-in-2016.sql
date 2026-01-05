# Write your MySQL query statement below
select round(sum(tiv_2016),2) as tiv_2016 from insurance
where tiv_2015 in (
    select tiv_2015 from insurance
    group by tiv_2015
    having count(tiv_2015)>1
)
and (lat,lon) in (
    select lat,lon from insurance
    group by lat,lon
    having count(*)=1
)


-- select round(sum(tiv_2016),2) as tiv_2016
-- from (
--     select tiv_2016,
--     count(*) over (partition by tiv_2015) as count_tiv_2015,
--     count(*) over (partition by lat,lon) as count_lat_lon
--     from insurance
-- ) as subquery
-- where count_tiv_2015>1 and count_lat_lon=1


