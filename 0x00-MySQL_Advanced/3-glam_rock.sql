-- Task: List all bands with Glam rock as their main style, ranked by their longevity
-- This script assumes the 'metal_bands.sql' table dump has been imported

-- Select and rank bands with Glam rock as their main style by their longevity
SELECT
    band_name,  -- Name of the band
    CASE
        WHEN split IS NULL THEN 2022 - formed  -- Calculate lifespan if the band hasn't split
        ELSE split - formed  -- Calculate lifespan if the band has split
    END AS lifespan  -- Lifespan of the band in years
FROM
    metal_bands  -- Table containing metal bands information
WHERE
    main_style = 'Glam rock'  -- Filter bands with Glam rock as their main style
ORDER BY
    lifespan DESC;
