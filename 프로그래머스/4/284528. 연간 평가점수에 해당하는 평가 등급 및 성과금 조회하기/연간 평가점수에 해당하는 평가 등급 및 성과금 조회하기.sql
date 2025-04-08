with base as
(
    select emp_no
        , avg(score) as avg_score
    from hr_grade
    group by 1
)
select he.emp_no
    , he.emp_name
    , case when avg_score >= 96 then 'S'
        when avg_score < 96 and avg_score >= 90 then 'A'
        when avg_score < 90 and avg_score >= 80 then 'B'
        else 'C' end grade
    , case when avg_score >= 96 then sal * 0.2
        when avg_score < 96 and avg_score >= 90 then sal * 0.15
        when avg_score < 90 and avg_score >= 80 then sal * 0.1
        else 0 end bonus
from hr_employees as he
join base as hg on he.emp_no = hg.emp_no 
order by 1;