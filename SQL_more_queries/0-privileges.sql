-- Script that
SELECT
    GRANTEE,
    PRIVILEGE_TYPE
FROM
    INFORMATION_SCHEMA.USER_PRIVILEGES
WHERE
    GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'");

