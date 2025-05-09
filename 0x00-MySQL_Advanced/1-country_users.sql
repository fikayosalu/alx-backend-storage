-- An SQL script that creates a users table and uses ENUM

CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY(id)
	);
