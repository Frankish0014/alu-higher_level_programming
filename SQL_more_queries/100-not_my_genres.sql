-- Select all genres that are not associated with the show 'Dexter'
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_shows_genres
    WHERE show_id = (
        SELECT id
        FROM tv_shows
        WHERE title = 'Dexter'
    )
)
ORDER BY name ASC; 
