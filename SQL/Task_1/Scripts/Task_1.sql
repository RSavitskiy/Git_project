SELECT Name, Surname
FROM countryinfo_user AS cu
JOIN  peopleinfo_user AS pu
ON cu.city_id = pu.city_id
WHERE isCapital=1
AND isOccupied=0
AND CountryName IN ("United Kingdom","Spain")





