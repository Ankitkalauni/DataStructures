/*
Table and views
1.create table
2.alter table
*/

show databases;
use movies;

show tables;

drop table if exists table1;
create table if not exists table1(id int primary key);
select * from table1;

-- alter table (add column)
alter table table1
add column first_name varchar(40);

select * from table1;

-- add multiple columns in existing columns
alter table table1
add column last_name varchar(40)
after id,
add column middle_name varchar(40)
after last_name;

select * from table1;

-- modify column in the table
alter table table1
modify first_name varchar(40) not null
first;

-- drop column in the table
alter table table1
drop column middle_name;


-- rename column in table
alter table table1
change column last_name surname varchar(40)
first;

-- rename table itself;
alter table table1
rename to movie_details;

show full tables;

show tables in movies;
show tables from movies;


-- filter tables search
show tables from movies like "movie%";

-- SHOW TABLES In mystudentdb WHERE Tables_in_mystudentdb= "employees";  

-- rename old table
show tables;

rename table movie_details to movies_df;
-- RENAME TABLE old_tab1 TO new_tab1,  
--             old_tab2 TO new_tab2, old_tab3 TO new_tab3;

alter table movies_df
rename to movies_temp;

-- How to RENAME Temporary Table (only stays for the session)
drop table if exists movies_temp;
create temporary table movies_temp(id int not null, name varchar(40));

insert into movies_temp(id, name) values (1, 'ankit kalauni'); -- insert values to the temp table

select * from movies_temp;

rename table movies_temp to movies_; -- will give error bcoz its a temp table

-- use alter for temp tables

alter table movies_temp
rename to movies_;

-- MySQL TRUNCATE Table
/*
The TRUNCATE statement in MySQL removes the 
complete data without removing its structure.
It is a part of DDL or data definition language command.
Generally, we use this command when we want to delete 
an entire data from a table without removing the 
table structure.

The TRUNCATE command works the same as a DELETE 
command without using a WHERE clause 
that deletes complete rows from a table.

for more info --> https://www.javatpoint.com/mysql-truncate-table
*/

show tables;
truncate table movies_info; -- cant truncate bcoz of foreign key referance;
-- truncate table table_name;

-- How to Truncate Table with Foreign key?
SET FOREIGN_KEY_CHECKS=0;
truncate table movies_info; -- will work fine
SET FOREIGN_KEY_CHECKS=1;  

-- How to truncate all tables in MySQL?
SELECT Concat('TRUNCATE TABLE ', TABLE_NAME) 
FROM INFORMATION_SCHEMA.TABLES  
WHERE table_schema = 'database_name'; 

-- MySQL DESCRIBE TABLE
show tables;
desc movies_info;
describe movies_info;

show columns from movies_info;
-- SHOW COLUMNS FROM database_name.table_name;  

-- MySQL EXPLAIN
explain select * from movies_info;

-- DROP IN MYSQL SERVER
-- DROP [ TEMPORARY ] TABLE [ IF EXISTS ] table_name [ RESTRICT | CASCADE ];  

drop temporary table if exists movies_temp;

-- DROP TABLE IF EXISTS table_name1, table_name2, table, ......., table_nameN;  

-- Syntax of Creating Temporary Table
create temporary table temp_table(id int not null);

/*
CREATE TEMPORARY TABLE temp_customers  
SELECT c.cust_name, c.city, o.prod_name, o.price   
FROM orders o  
INNER JOIN customer c ON c.cust_id = o.order_id  
ORDER BY o.price DESC;  

DROP TEMPORARY TABLE table_name; 
*/

-- MySQL Copy/Clone/Duplicate Table
/*
CREATE TABLE new_table_name  
SELECT column1, column2, column3   
FROM existing_table_name;  
*/

create table if not exists table_temp
select id
from movies_info;

-- CREATE TABLE IF NOT EXISTS new_table_name LIKE existing_table_name;  -- copy structure
-- INSERT new_table_name SELECT * FROM existing_table_name;  -- copy data

/*
CREATE TABLE IF NOT EXISTS duplicate_table   
SELECT * FROM original_table WHERE Year = '2016';  
*/