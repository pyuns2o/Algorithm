-- 코드를 입력하세요
SELECT ao.animal_id
    , ao.name
from animal_outs as ao
left join animal_ins as ai on ao.animal_id = ai.animal_id
where 1=1
    and ai.animal_id is null
order by 1;