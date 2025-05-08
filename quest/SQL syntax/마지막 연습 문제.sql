-- 44
select *
from products p
inner join orders o on p.id=o.product_id

-- 45(살짝 어려움)
select p.id,
    sum(p.price*o.quantity) total_sales
from products p
inner join orders o on p.id=o.product_id
group by p.id
order by total_sales desc
limit 1 

-- 46
select p.id,
        sum(o.quantity) total_quantity
from products p
inner join orders o on p.id=o.product_id
group by p.id

-- 47
select *
from products p
inner join orders o on p.id=o.product_id
where order_date > "2023-03-03"

-- 48
select name,
        sum(o.quantity) total_quantity
from products p
inner join orders o on p.id=o.product_id
group by p.id
order by total_quantity desc
limit 1 

-- 49
select p.id,
        avg(o.quantity) avg_quantity
from products p
inner join orders o on p.id=o.product_id
group by p.id

-- 50
select p.id,
        p.name
from products p
left join orders o on p.id=o.product_id
where o.quantity is null