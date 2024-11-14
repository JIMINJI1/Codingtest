#임시테이블(0-23시간)
WITH RECURSIVE hour_list AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1 
    FROM hour_list 
    WHERE HOUR < 23
)
SELECT 
    hl.HOUR,
    COUNT(ao.ANIMAL_ID) AS COUNT
FROM 
    hour_list hl
LEFT JOIN 
    ANIMAL_OUTS ao ON hl.HOUR = HOUR(ao.DATETIME)
GROUP BY 
    hl.HOUR
ORDER BY 
    hl.HOUR;
