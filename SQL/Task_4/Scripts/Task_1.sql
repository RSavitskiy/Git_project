SELECT DISTINCT Name AS projects, a.e_id AS employees FROM project AS p
JOIN assign AS a
ON a.p_id = p.p_id
WHERE a.e_id IS NULL
