with base as
(
    select b.author_id
    , b.book_id
    , b.category
    , b.price
    , sum(sales) as sales_cnt
    , (price * sum(sales)) as sales_amt
    from book as b
    left join book_sales as bs on b.book_id = bs.book_id
        and date_format(bs.sales_date, '%Y-%m') = '2022-01'
    group by 1,2,3,4
)
select a.author_id 
    , a.author_name
    , category
    , sum(sales_amt) as total_sales
from base as b
join author as a on b.author_id = a.author_id
group by 1,2,3
order by 1, 3 desc;
    