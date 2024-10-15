SELECT 
    i.REST_ID, 
    i.REST_NAME, 
    i.FOOD_TYPE, 
    i.FAVORITES, 
    i.ADDRESS, 
    ROUND(AVG(r.REVIEW_SCORE), 2) AS score
FROM 
    REST_INFO i
JOIN 
    REST_REVIEW r ON i.REST_ID = r.REST_ID
WHERE 
    i.ADDRESS LIKE '서울%'
GROUP BY 
    i.REST_ID, 
    i.REST_NAME, 
    i.FOOD_TYPE, 
    i.FAVORITES, 
    i.ADDRESS
ORDER BY 
    score DESC, 
    i.FAVORITES DESC;