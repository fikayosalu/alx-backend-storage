-- An SQL script that creates a users table

CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255) UNIQUE,
	PRIMARY KEY(id)
	);
