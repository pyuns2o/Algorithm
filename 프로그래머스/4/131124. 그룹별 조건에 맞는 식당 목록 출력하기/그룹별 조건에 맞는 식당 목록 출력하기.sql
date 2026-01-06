with review as
(
    select member_id
        , count(review_id) as review_cnt
    from rest_review
    group by 1
    order by 2 desc
    limit 1
)

select m.member_name
    , r.review_text
    , date_format(r.review_date, '%Y-%m-%d') as review_date
from rest_review as r
join member_profile as m on r.member_id = m.member_id
where m.member_id = (select member_id from review)
order by 3, 2;