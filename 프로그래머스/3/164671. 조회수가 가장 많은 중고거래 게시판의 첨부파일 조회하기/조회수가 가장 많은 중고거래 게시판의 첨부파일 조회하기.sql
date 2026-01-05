-- 코드를 입력하세요
with high_view as
(
    select board_id
    from used_goods_board
    where views = (select max(views) from used_goods_board)
)

select concat('/home/grep/src/' , ugf.board_id, '/' , file_id , file_name , file_ext) as file_path
from used_goods_file as ugf
join high_view as h on ugf.board_id = h.board_id
order by file_id desc;