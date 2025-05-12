-- 코드를 입력하세요
with base as
(
    select cc.car_id
        , cc.car_type
        , cc.daily_fee
        , cd.discount_rate
    from CAR_RENTAL_COMPANY_CAR as cc
    join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as cd on cc.car_type = cd.car_type
        and cd.duration_type = '30일 이상'
    where 1=1
        and cc.car_type in ('세단', 'SUV')
)
, nov_list as
(
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where 1=1
        and start_date <= '2022-11-30'
        and end_date >= '2022-11-01'
)
select car_id
    , car_type
    , floor((100-discount_rate)/100 * daily_fee * 30) as fee
from base
where 1=1
    and floor((100-discount_rate)/100 * daily_fee * 30) >= 500000
    and floor((100-discount_rate)/100 * daily_fee * 30) < 2000000
    and car_id not in (select car_id from nov_list)
order by 3 desc, 2, 1 desc;
