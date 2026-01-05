-- 코드를 입력하세요
with threeup as
(
    select writer_id
        , count(distinct board_id) as writing_count
    from used_goods_board
    group by 1
    having writing_count >= 3
)

select user_id
    , nickname
    , concat(city,' ',street_address1,' ' ,street_address2) as '전체주소'
    , concat(left(TLNO,3), '-', substring(TLNO,4,4) , '-', right(TLNO,4)) as '전화번호'
from used_goods_user as u
join threeup as t on u.user_id = t.writer_id
order by 1 desc;