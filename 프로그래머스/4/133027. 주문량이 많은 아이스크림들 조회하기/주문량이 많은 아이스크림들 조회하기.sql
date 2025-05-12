with july_order as
(
    select flavor
        , sum(total_order) as july_cnt
    from july
    group by 1
)
, total_order as
(
    select j.flavor
        , (july_cnt + total_order) as total_cnt
    from first_half as f
    left join july_order as j on j.flavor = f.flavor
    group by 1
)
, rnk as
(
    select flavor
        , rank() over (order by total_cnt desc) as rnk
    from total_order
)
select flavor
from rnk
where 1=1
    and rnk <= 3