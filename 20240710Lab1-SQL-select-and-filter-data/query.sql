-- 1
SELECT * FROM movies;

-- 2
SELECT title, release_year FROM movies;

-- 3
SELECT * FROM movies WHERE release_year >= 2000;

-- 4
SELECT * FROM movies WHERE genre = 'Action';

-- 5
SELECT COUNT(*) FROM movies;

-- 6
SELECT COUNT(DISTINCT genre) FROM movies;

-- 7
SELECT * FROM movies WHERE release_year BETWEEN 1990 AND 2000;

-- 8
SELECT * FROM movies WHERE genre = 'Drama' OR release_year <= 1990;

-- 9
SELECT * FROM movies WHERE title LIKE 'THE%';

-- 10
SELECT * FROM movies WHERE title NOT LIKE '%Love%';

-- 11
SELECT * FROM movies WHERE genre IN ('Action', 'Drama', 'Fantasy');

-- 12
SELECT * FROM movies WHERE genre = 'Fantasy' AND release_year BETWEEN 2005 and 2015;

-- 13
SELECT genre, COUNT(*) AS movie_count FROM movies GROUP BY genre;

-- 14
SELECT * FROM movies WHERE release_year >= 2000 LIMIT 10;

-- 15
SELECT * FROM movies WHERE title LIKE '%Star%';

-- 16
SELECT DISTINCT release_year FROM movies;

-- 17
SELECT genre, COUNT(*) AS movie_count FROM movies GROUP BY genre HAVING COUNT(*) > 50;

-- 18
SELECT * FROM movies WHERE genre <> 'Fantasy';

-- 19
SELECT * FROM movies WHERE release_year is NULL;

-- 20
SELECT * FROM movies WHERE release_year = 1990;