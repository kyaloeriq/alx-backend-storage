-- Script to create a trigger that decreases the quantity of an item after adding a new order

-- Task: Create a trigger to automatically update the quantity of an item in the 'items' table when a new order is inserted into the 'orders' table.

DELIMITER $$

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity of the item in the 'items' table
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE item_id = NEW.item_id;
END$$

DELIMITER ;
