SELECT h.FLAVOR
FROM FIRST_HALF h
LEFT JOIN JULY j ON h.FLAVOR = j.FLAVOR
GROUP BY h.FLAVOR, h.TOTAL_ORDER
ORDER BY SUM(j.TOTAL_ORDER) + h.TOTAL_ORDER DESC
LIMIT 3;