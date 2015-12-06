SELECT sum(e.Salary) AS Salary, p.Name AS Project FROM empl AS e
JOIN assign AS a
ON e.e_id= a.e_id
JOIN project AS p
ON a.p_id= p.p_id
GROUP BY p.name
HAVING SUM(e.Salary)< 1000

