-- 코드를 입력하세요
SELECT ai.animal_id
    , ai.name
from animal_ins as ai
left join animal_outs as ao on ai.animal_id = ao.animal_id
where 1=1
    and ai.datetime > ao.datetime
order by ai.datetime