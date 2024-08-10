-- Script to create a trigger that resets the attribute 'valid_email' only when the email has been changed

-- Task: Create a trigger to automatically reset the 'valid_email' attribute to false when the 'email' field is updated.

DELIMITER $$

CREATE TRIGGER reset_valid_email_after_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has changed
    IF NEW.email <> OLD.email THEN
        -- Reset the 'valid_email' attribute to false
        SET NEW.valid_email = FALSE;
    END IF;
END$$

DELIMITER ;
