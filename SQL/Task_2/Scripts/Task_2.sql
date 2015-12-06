SELECT SUM(Price) AS Price_repetitive_elements FROM orders
WHERE Status IN (SELECT Status FROM orders GROUP BY Status HAVING count(*)>1);