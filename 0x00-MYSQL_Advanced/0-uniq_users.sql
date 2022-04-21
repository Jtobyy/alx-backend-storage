-- We are all unique!
-- Making an attribute unique directly in the table schema will enforced your
-- business rules and avoid bugs in your application
CREATE TABLE IF NOT EXISTS users
(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
email varchar(255) UNIQUE NOT NULL, name varchar(255));
