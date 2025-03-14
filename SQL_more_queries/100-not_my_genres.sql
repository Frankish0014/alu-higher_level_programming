-- genres not linked to Dexter
SELECT name
FROM `tv_genres`
WHERE id NOT IN (
	SELECT genre_id
