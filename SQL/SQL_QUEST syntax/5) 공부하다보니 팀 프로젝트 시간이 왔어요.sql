-- 17
select name
from team_projects
where aws_cost >= 40000
-- 18
select *
from team_projects
where YEAR(start_date)=2022
-- 19
select *
from team_projects
where CURDATE() between start_date and end_date
-- CURDATE() 함수는 현재 날짜를 반환하는 함수
-- NOW() 함수는 현재 시각까지 반환하는 함수

-- 20
select id,
        name,
        DATEDIFF(end_date, start_date) duration_days
from team_projects
-- DATEDIFF() 함수는 두 날짜 사이의 일 수 차이를 계산

