-- This project shows us how to list the duplicate scores by showing how many times they appear as a label
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC ;
