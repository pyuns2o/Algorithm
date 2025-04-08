SELECT ri.rest_id as REST_ID
    , ri.rest_name as REST_NAME
    , ri.food_type as FOOD_TYPE
    , ri.favorites as FAVORITES
    , ri.address as ADDRESS
    , round(avg(rr.review_score),2) as SCORE
from rest_info as ri
join REST_REVIEW as rr on ri.rest_id = rr.rest_id
where 1=1
    and ri.address like '서울%'
group by 1,2,3,4,5
order by 6 desc, 4 desc;