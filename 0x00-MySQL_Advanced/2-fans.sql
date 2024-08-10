SELECT
    origin,  -- Country of origin of the band
    SUM(nb_fans) AS total_fans  -- Sum of non-unique fans per country
FROM
    metal_bands  -- Table containing metal bands information
GROUP BY
    origin  -- Grouping by country of origin
ORDER BY
    nb_fans DESC;  -- Ordering results by the total number of fans in descending order
