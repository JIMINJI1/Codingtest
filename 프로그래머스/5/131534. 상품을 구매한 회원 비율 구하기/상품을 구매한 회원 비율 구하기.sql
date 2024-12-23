SELECT
    YEAR (SALES_DATE) YEAR, 
    MONTH (SALES_DATE) MONTH, 
    COUNT (DISTINCT o.USER_ID) PURCHASED_USERS, 
    Round(COUNT (DISTINCT o.USER_ID)/(SELECT COUNT (*) FROM USER_INFO WHERE JOINED LIKE '2021%'), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE o JOIN USER_INFO u
ON o.USER_ID = u.USER_ID
WHERE JOINED LIKE '2021%'
GROUP BY 1, 2
ORDER BY 1, 2