USE bookstore;

SELECT * FROM books_sold;

DROP TABLE books_sold;

CREATE TABLE books_sold
(
    date_sold date,
    Calgary_store_quantity int,
    Edmonton_store_quantity int,
    RedDeer_store_quantity int
);

INSERT INTO books_sold (date_sold, Calgary_store_quantity,  Edmonton_store_quantity, RedDeer_store_quantity)
VALUES ('2024-01-19', 11, 8, 8),
('2024-01-18', 30, 20, 6),
('2024-01-17', 15, 8, 7),
('2024-01-16', 25, 12, 1),
('2024-01-15', 2, 10, 78),
('2024-01-14', 10, 28, 0),
('2024-01-13', 10, 28, 0);


SELECT *,
CASE
	WHEN pages > 200 THEN "big"
    ELSE "small"
END AS size
FROM books;

SELECT *,
CASE
	WHEN stock_quantity < 100 THEN "low stock"
    WHEN stock_quantity < 500 THEN "medium stock"
    ELSE "high stock"
END AS stock_status
FROM books;

SELECT title, stock_quantity,
CASE
	WHEN stock_quantity <= 50 THEN "Needs stock up"
    WHEN stock_quantity <= 100 THEN "Stock is okay"
    ELSE "Overstock"
END AS stock_status
FROM books;
