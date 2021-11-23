-- Prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL.

USE information_schema;

SELECT TABLE_NAME 'Table', COLUMN_NAME 'Field', COLUMN_TYPE 'Type', IS_NULLABLE 'Null',
	COLUMN_KEY 'Key', COLUMN_DEFAULT 'Default', EXTRA 'Extra'
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0'
ORDER BY TABLE_NAME;
