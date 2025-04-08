-- 코드를 작성해주세요
with first_gen as
(
    select id
    from ecoli_data
    where 1=1
        and parent_id is null
)
, second_gen as
(
    select e.id
    from ecoli_data as e
    join first_gen as f on e.parent_id = f.id
)

select e.id
from ecoli_data as e
join second_gen as s on e.parent_id = s.id