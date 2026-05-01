  with recursive numbers as(
       select  1 as num
        union all
       select num+1
       from numbers
        where num<10)
  select * from numbers 

  --to find the missing numbers in a series by using recursive cte
  with recursive seq as(
    select min(num) as n
    from numbers
    union all 
    select n+1
    from seq
    where n < (select max(num)from numbers)
  )

  select n as missing_number                  select s.n as missing_number
  from seq                                    from seq s
  where n not in (select num from numbers)    left join numbers n 
  order by n                                     on s.n=t.num 
                                               where t.num is null
                                               order by s.n;   