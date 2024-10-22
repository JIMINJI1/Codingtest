SELECT CONCAT('/home/grep/src/', b.board_id, '/', f.file_id, f.file_name, f.file_ext) AS FILE_PATH
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_FILE f ON b.board_id = f.board_id
WHERE b.board_id = (
    SELECT board_id
    FROM USED_GOODS_BOARD
    ORDER BY views DESC
    LIMIT 1
)
ORDER BY f.file_id DESC;
