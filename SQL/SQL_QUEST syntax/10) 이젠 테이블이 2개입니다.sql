-- 38
select count(*)
from departments

-- 39
select e.name,
        d.name
from employees e inner join departments d on e.department_id=d.id

-- 40
select e.name
from employees e inner join departments d on e.department_id=d.id
where d.name='기술팀'

-- 41(어려움)

SELECT d.name, COUNT(*) AS employee_count
FROM employees e
left JOIN departments d ON e.department_id = d.id
GROUP BY d.name;

-- 42(어려움)
select d.name
from employees e
left join departments d on e.department_id=d.id
where e.id is null

-- 43
select e.name
from employees e
inner join departments d on e.department_id=d.id
where d.name="마케팅팀"