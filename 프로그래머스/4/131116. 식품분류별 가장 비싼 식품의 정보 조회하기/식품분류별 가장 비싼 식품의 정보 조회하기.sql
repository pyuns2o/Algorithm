with rnk as
(
    select category
        , price
        , product_name
        , rank() over (partition by category order by price desc) as rnk
    from food_product
)
select category
    , price as max_price
    , product_name
from rnk
where 1=1
    and rnk = 1
    and category in ('과자', '국', '김치', '식용유')
order by price desc;