-- Script to create a stored procedure 'AddBonus' that adds a new correction for a student

-- Task: Create a stored procedure that takes 'user_id', 'project_name', and 'score' as inputs, 
-- checks if the project exists, and adds a new correction for the student.

DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score DECIMAL(5,2)
)
BEGIN
    DECLARE project_id INT;

    -- Check if the project already exists
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    -- If the project does not exist, create it
    IF project_id IS NULL THEN
        INSERT INTO projects (name)
        VALUES (project_name);
        
        -- Get the id of the newly created project
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Add a new correction for the student
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END$$

DELIMITER ;
