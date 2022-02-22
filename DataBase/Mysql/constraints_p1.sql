/*
Constraints part-1 practice

Notes - we can use constraints key word to give names to the any constraints later
we can use this name to drop that constraints and to modify

syntax - add constraint constraint_name unique(id) int not null;

____

we can alter tabel and modify, drop and add constraints to the existing columns of tabel.
we can also specify constraints while init the table with its columns.


What is schema in SQL with example?
A schema is a collection of database objects like tables, triggers, stored procedures, etc.
A schema is connected with a user which is known as the schema owner. ...
SQL Server have some built-in schema, for example: dbo, guest, sys, and INFORMATION_SCHEMA.
dbo is default schema for a new database, owned by dbo user.02-Sept-2020

information_schema.KEY_COLUMN_USAGE - https://stackoverflow.com/questions/5094948/mysql-how-can-i-see-all-constraints-on-a-table/25116973
*/



show databases;
use movies;
show tables;

drop table if exists movies_info;

create table movies_info(
id int not null,
first_name varchar(25) not null,
last_name varchar(25) not null,
constraint u_name unique(id, last_name)
);

show tables;



select *,whole_name from movies_info;
desc movies_info;

alter table movies_info
add count int not null unique auto_increment first;

alter table movies_info
drop constraint u_name;


alter table movies_info
add constraint whole_name unique(first_name, last_name);

alter table movies_info
modify id int not null unique;

alter table movies_info
drop index whole_name;

show table status;

select *
from information_schema.KEY_COLUMN_USAGE
where TABLE_NAME = 'movies_info';