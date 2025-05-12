-- 코드를 입력하세요
select fp.product_id
    , fp.product_name
    , sum(price * amount) as total_sales
from food_order as fo
join food_product as fp on fo.product_id = fp.product_id
    and date_format(fo.produce_date, '%Y-%m') = '2022-05'
group by 1,2
order by 3 desc, 1;
