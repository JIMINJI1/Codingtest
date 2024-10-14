select  date_format(o.sales_date,'%Y') as year, date_format(o.sales_date,'%m') as month, u.gender,
count (distinct u.user_id) as users
from USER_INFO u
join online_sale o on u.user_id = o.user_id
where u.gender in (0,1)
GROUP BY year, month, u.GENDER
ORDER BY year, month, u.GENDER;