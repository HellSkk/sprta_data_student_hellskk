-- 13
select name,
        track
from sparta_students
-- 14
select *
from sparta_students
where track<>'Unity'
-- 15
select *
from sparta_students
where enrollment_year in (2021, 2023)
-- 16
select *
from sparta_students
where track='Node.js' and grade='A'