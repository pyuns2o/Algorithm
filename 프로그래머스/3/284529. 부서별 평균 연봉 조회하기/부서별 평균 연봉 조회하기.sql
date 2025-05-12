select he.dept_id
    , hd.dept_name_en
    , round(avg(he.sal),0) as avg_sal
from hr_employees as he
join hr_department as hd on he.dept_id = hd.dept_id
group by 1,2
order by 3 desc;