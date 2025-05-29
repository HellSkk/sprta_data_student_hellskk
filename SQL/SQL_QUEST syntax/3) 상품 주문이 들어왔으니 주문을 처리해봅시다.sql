-- 9
select customer_id
from orders
where amount>=2
-- 10
select *
from orders
where order_date > '2023-11-02' and amount >= 2
-- 11
select *
from orders
where amount<3 and shipping_fee>15000
-- 12
select *
from orders
order by shipping_fee desc
