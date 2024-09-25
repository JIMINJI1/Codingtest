-- 코드를 입력하세요
SELECT CATEGORY, PRICE, PRODUCT_NAME
FROM (
    SELECT F.CATEGORY, F.PRICE, F.PRODUCT_NAME,
           ROW_NUMBER() OVER (PARTITION BY F.CATEGORY ORDER BY F.PRICE DESC) AS RANKING
    FROM FOOD_PRODUCT F
    WHERE F.CATEGORY IN ('과자', '국', '김치', '식용유')
)
WHERE RANKING = 1
ORDER BY PRICE DESC;
