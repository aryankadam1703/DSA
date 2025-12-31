# Write your MySQL query statement below
with Total_product as(
    select customer_id,count(distinct product_key) as total
    from customer
    group by customer_id
)
select customer_id from Total_product t
where t.total=(select count(*) from Product);