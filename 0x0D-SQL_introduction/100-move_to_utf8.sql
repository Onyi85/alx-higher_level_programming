-- This project teaches us how to convert the entire table to utf8 character set
-- select the database first
USE hbtn_0c_0;
-- first convert the database hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name BLOB;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
