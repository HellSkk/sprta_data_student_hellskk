-- 30
select name
from doctors
where major='성형외과'

-- 31
select major,
        count(*)
from doctors
group by major

-- 32
select count(*)
from doctors
where hire_date <= DATE_SUB(CURDATE(), INTERVAL 5 YEAR);
-- 이 함수는 현재 기준 5년 전의 날짜를 반환하고 그 날짜보다 적은 날짜를 반환한다
-- DATE_SUB은 지정한 날짜에서 주어진 시간 간격을 빼는 함수다
-- INTERVAL 5 YEAR은 날짜에서 5년을 빼는 간격을 의미한다


-- 33
select DATEDIFF(CURDATE(), hire_date) working_days
from doctors