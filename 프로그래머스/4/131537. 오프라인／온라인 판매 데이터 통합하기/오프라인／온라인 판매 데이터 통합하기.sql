with base as
(
    -- online
    (select sales_date
        , product_id
        , user_id
        , sales_amount
    from online_sale)
    union all
    -- offline
    (select sales_date
        , product_id
        , null as user_id
        , sales_amount
     from offline_sale
    )
)
select date_format(sales_date, '%Y-%m-%d') as SALES_DATE
    , PRODUCT_ID
    , USER_ID
    , sum(sales_amount) as SALES_AMOUNT
from base
where 1=1
    and date_format(sales_date, '%Y-%m') = '2022-03'
group by 1,2,3
order by 1,2,3