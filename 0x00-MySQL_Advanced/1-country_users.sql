-- creates a table 'users' with specified attributes
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country VARCHAR(2) NOT NULL DEFAULT 'US'
);
ALTER TABLE users
ADD CONSTRAINT country_enum CHECK (country IN ('US', 'CO', 'TN'));
