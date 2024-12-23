SELECT 
    C.CAR_ID, 
    C.CAR_TYPE, 
    ROUND(C.DAILY_FEE * 30 * (1 - COALESCE(P.DISCOUNT_RATE, 0) / 100), 0) AS FEE
FROM 
    CAR_RENTAL_COMPANY_CAR C
LEFT JOIN 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY H 
    ON C.CAR_ID = H.CAR_ID 
    AND (H.START_DATE <= '2022-11-30' AND H.END_DATE >= '2022-11-01')
LEFT JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
    ON C.CAR_TYPE = P.CAR_TYPE 
    AND P.DURATION_TYPE = '30일 이상'
WHERE 
    C.CAR_TYPE IN ('세단', 'SUV')
    AND H.HISTORY_ID IS NULL 
    AND ROUND(C.DAILY_FEE * 30 * (1 - COALESCE(P.DISCOUNT_RATE, 0) / 100), 0) 
        BETWEEN 500000 AND 2000000
ORDER BY 
    FEE DESC, 
    C.CAR_TYPE ASC, 
    C.CAR_ID DESC;