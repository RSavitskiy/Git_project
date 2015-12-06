SELECT Name, Status FROM customers AS c
JOIN orders AS o
ON c.CustomersID = o.CustomerID;
