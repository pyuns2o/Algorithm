with base as
(
    select ui.user_id
        , ui.gender
        , os.sales_date
    from user_info as ui
    join online_sale as os on ui.user_id = os.user_id
)
select date_format(sales_date, '%Y') as year
    , date_format(sales_date, '%m') as month
    , gender
    , count(distinct user_id) as users
from base
where 1=1
    and gender is not null
group by 1,2,3
order by 1,2,3