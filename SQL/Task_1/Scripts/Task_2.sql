SELECT COUNT(Name) AS Quantity FROM PeopleInfo_user AS pu
JOIN CountryInfo_user AS cu
ON cu.City_id = pu.City_id
WHERE isCapital = 0
AND isOccupied = 0
AND Population >= 1000000
AND CountryName IN ('Poland','Ukraine')
