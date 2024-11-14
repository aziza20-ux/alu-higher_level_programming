-- Create user_0d_1 as a root user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;


CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;


REVOKE ALL PRIVILEGES ON `user_2_db`.* FROM 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON `user_2_db`.* TO 'user_0d_2'@'localhost';
