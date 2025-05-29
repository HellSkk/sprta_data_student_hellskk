-- 21
select id,
        name,
        region,
        rating,
        RANK() OVER (ORDER BY rating desc) rating_rank
from lol_users
-- RANK() 함수는 동점자에게 같은 순위를 부여하고 다음 순위를 건너 뜀
-- DESNE_RANK() 함수는 동점자에게 같은 순위를 부여하되 건너뛰지 않음

-- 22
select name
from lol_users
order by join_date desc
limit 1
-- LIMIT 함수는 결과에서 가져올 행의 개수를 제한하는 명령

-- 23
select name,
        region,
        rating
from lol_users
order by region, rating desc
-- group by region 으로 했었는데 그 경우에는 원치 않은 결과가 나올 수도 있다고 함

-- 24
select name,
        region,
        avg(rating)
from lol_users
group by region
