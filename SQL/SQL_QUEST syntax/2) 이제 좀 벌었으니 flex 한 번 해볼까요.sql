-- 5
select product_name,
        price
from products
-- 6
select *
from products
where product_name LIKE '%프로'
-- 7
select *
from products
where producdt_name LIKE '갤%'

select sum(price) total_price
from products
