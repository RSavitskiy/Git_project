SELECT c.Name, o.OrderID, co.Name FROM orders AS o
JOIN customers AS c
ON c.CustomersID = o.CustomerID
JOIN country AS co
ON c.CountryID=co.ID
