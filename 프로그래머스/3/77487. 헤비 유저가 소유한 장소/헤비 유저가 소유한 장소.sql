SELECT * FROM places
WHERE host_id IN (SELECT host_id FROM places GROUP BY host_id  HAVING COUNT(id) >= 2)
ORDER BY id;
