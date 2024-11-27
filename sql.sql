CREATE DATABASE user_db;

USE user_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(15),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255)
);

SELECT * FROM users;

SELECT * FROM users;

INSERT INTO users (first_name, last_name, phone, username, password)
VALUES ('SHARAN','T G', 7904499758, 'SHARAN0308',5555 );


GRANT INSERT ON user_db.users TO 'root'@'localhost';

GRANT SELECT, INSERT, UPDATE ON user_db.users TO 'root'@'localhost';

GRANT ALL PRIVILEGES ON user_db.* TO 'root'@'localhost';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'root'@'localhost';
