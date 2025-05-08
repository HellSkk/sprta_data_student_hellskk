-- 34
select gender,
        count(*)
from patients
group by gender

-- 35
select count(*)
from patients
where birth_date <= DATE_SUB(CURDATE() INTERVAL 40 YEAR)

-- 36
select *
from patients
where last_visit_date <= DATE_SUB(CURDATE() INTERVAl 1 YEAR)

-- 37
select count(*)
from patients
where birth_date between '1980-01-01' and '1989-12-31'
