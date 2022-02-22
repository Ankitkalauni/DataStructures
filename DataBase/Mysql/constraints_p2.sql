/*
practice day 2


user defire variables;
we can use:- set @varname = value and also set @varname := value

more about constraints.

not null and unique key;
primary and foreign key;
Check and Default constraits;

*/

-- user define variables
set @pi := 3.147; -- set @pi := 3.147
set @full_name := "Ankit Kalauni";
select @pi;

show databases;
use world;
show tables;

-- using user define variable...
select @popu:= max(Population) as "Max Population" from city;

-- un declare user define variable will give null
select @surname;

-- local variables use DECLARE. use DEFAULT to give default value or else it will give null value 
-- DECLARE variable_name datatype(size) [DEFAULT default_value];
-- (can only be use inside store-procedure)
-- declare father_name varchar(40) default "yamraj";

-- System Variable
/*
System variables are a special class to all program units, which contains predefined variables.
MySQL contains various system variables that configure its operation, and each system variable contains a default value.
We can change some system variables dynamically by using the SET statement at runtime.
It enables us to modify the server operation without stop and restart it.
The system variable can also be used in the expressions.
*/

show variables; -- or
-- select @@var_name;

show variables like '%wait_timeout%';

select @@key_buffer_size;


select "Below practice is from Krish Naik video" as "INFO";

-- seeing all database
show databases;

-- using specific database 
use movies;

-- seeing all tables created inside the database(schema)
show tables;

-- droping tabel if it exist else pass
drop table if exists movies_info;

-- creating new tabel movies_info
create table movies_info(id int,
constraint prime primary key(id));

-- describe the table information similar like pandas describe
describe movies_info; -- desc movies_info;

-- alter table and add new columns with changing constraints
alter table movies_info
add director varchar(40),
change director director int not null;

-- How to add column if not exits in column
-- IF NOT EXISTS( SELECT NULL
--             FROM INFORMATION_SCHEMA.COLUMNS
--            WHERE table_name = 'tablename'
--              AND table_schema = 'db_name'
--              AND column_name = 'columnname')  THEN

--   ALTER TABLE `TableName` ADD `ColumnName` int(1) NOT NULL default '0';

-- END IF;

select * from movies_info;

-- alter table
alter table movies_info
drop director;

-- showing text as in the info table with row value given in ""
SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

-- delete table if exits
drop table if exists movies_cast;

-- creating new table to learn about foreign key
create table movies_cast(movie_id int,cast_name varchar(40) not null,
constraint foreignn foreign key(movie_id) references movies_info(id));

-- seeing all columns inside table specified
select * from movies_info, movies_cast;

desc movies_cast;

-- check constraints is use to validate the input value and sote the verified value only;
-- like check(salary < 50000)
-- default constraint is use to give default value to the column
alter table movies_cast
add movie_budget int not null check(movie_budget > 50000) default 0;

desc movies_info;
desc movies_cast;


