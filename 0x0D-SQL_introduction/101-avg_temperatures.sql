-- This project displays the average temperature in Fahrenheit unit in the city ordered by the calculated value in descending order

SELECT city, AVG(value) AS avg_temp
FROM temperature 
GROUP BY city 
ORDER BY avg_temp DESC;
