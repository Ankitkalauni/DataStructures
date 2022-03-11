/*
indexes in mysql

1. index is used speed up queries.
2. Insert and updates will be slow.
*/

use movies; -- database
show tables;

select * from movies_info;

alter table movies_info
add column movie_name varchar(40);

create index index_movie
on movies_info(id); -- table_name(column)

create index index_id_and_name
on movies_info(id, movie_name); -- index 2 columns

alter table movies_info
drop index index_id_and_name,
drop index index_movie;

desc movies_info;


/*
View in MYSQL
A view is a database object that has no values.
Its contents are based on the base table.
It contains rows and columns similar to the real table.
In MySQL, the View is a virtual table created by a
query by joining one or more tables.


NOTE - VIEW ONLY WORKS WITH SOME SPECIFIC QUERIES

SQL Joins

1. inner join
2. left join
3. right join
4. full join
5. natural join
6. cross join

*/
show databases;

use movies;

show tables;

select * from movies_info;
desc movies_info;

alter table movies_info
modify movie_name varchar(40) not null;

insert into movies_info values(1, "Phir Hera Pheri"),(2, "Hera Pheri"),
(3,'Macho man');


create view movies_information as
select * from movies_info;

select * from movies_information;

drop view movies_information;

-- sql joins

show databases;

use movies;

show tables;
