docker run --name test-postgres \
  -e POSTGRES_USER=test_user \
  -e POSTGRES_PASSWORD=test_password \
  -e POSTGRES_DB=test_db \
  -p 5432:5432 \
  -d postgres:16




CREATE TABLE posts (
    id INT PRIMARY KEY,
    title VARCHAR,
    content VARCHAR,
    published BOOLEAN,
    created_at TIMESTAMP
);

ALTER TABLE posts
ALTER COLUMN created_at SET DEFAULT NOW();

INSERT INTO posts (id, title, content, published, created_at)
VALUES
    (1, 'First', 'Privet', true, current_timestamp),
    (2, 'Second', 'HRU', false, CURRENT_TIMESTAMP),
    (3, 'Third', 'good', true, current_timestamp);

SELECT * FROM posts;

SELECT * FROM posts WHERE id = 2;

UPDATE posts
SET published = true
WHERE id = 2

-- DROP TABLE orders;
