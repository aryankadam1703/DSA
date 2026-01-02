# Write your MySQL query statement below

-- select x,y,z,                                    My Approach
-- case 
--     when greatest(x,y,z) = x and y+z>x
--     then 'Yes'
--     when greatest(x,y,z) = y and x+z>y
--     then 'Yes'
--     when greatest(x,y,z) = z and x+y>z
--     then 'Yes'
--     else 'No'
-- end as triangle
-- from Triangle


select *, if(x+y>z and y+z>x and x+z>y,'Yes','No') as triangle from Triangle

