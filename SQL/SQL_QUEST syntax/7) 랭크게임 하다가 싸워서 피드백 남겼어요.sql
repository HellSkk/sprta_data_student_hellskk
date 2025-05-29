-- 25
select *
from lol_feedbacks
order by satisfaction_score desc

-- 26
SELECT user_name, 
        MAX(feedback_date) 
FROM lol_feedbacks 
GROUP BY user_name;

-- 27
select count(*)
from lol_feedbacks
where satisfaction_score = 5

-- 28
select user_name,
        count(*) cnt_feedbacks
from lol_feedbacks
group by user_name
order by cnt_feedbacks desc
limit 3

-- 29
select feedback_date,
        avg(satisfaction_score) avg_satisfaction_score
from lol_feedbacks
group by feedback_date
order by avg_satisfaction_score desc
limit 1
