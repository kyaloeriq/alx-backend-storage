-- Task: Rank country origins of bands, ordered by the number of (non-unique) fans
-- This script assumes the 'metal_bands.sql' table dump has been imported

-- Select and rank country origins by the total number of non-unique fans
SELECT 
    origin,  -- Country of origin of the band
    SUM(nb_fans) AS total_fans  -- Sum of non-unique fans per country
FROM 
    metal_bands  -- Table containing metal bands information
GROUP BY 
    origin  -- Grouping by country of origin
ORDER BY 
    total_fans DESC;  -- Ordering results by the total number of fans in descending order
