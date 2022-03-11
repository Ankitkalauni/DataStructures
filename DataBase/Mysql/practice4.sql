/*
practice 4
1. databases basic commands.
	create --> select --> show --> drop --> copy

2. table columns.
	add --> modify --> drop --> rename

*/

create database if not exists temp;
show databases;
show schemas;
select schema_name from information_schema;
use temp;
drop database if exists temp;
drop schema if exists temp;

-- mysqldump -u root p testdb path\testdb.sql

-- ____________________________________________
/*
CREATE TABLE [IF NOT EXISTS] table_name(  
    column_definition1,  
    column_definition2,  
    ........,  
    table_constraints  
);  

*/
create database if not exists temp;
use temp;

drop table if exists temp_table;

create table if not exists temp_table(
	col1 int,
    col2 varchar(12),
    col3 longtext
    );
    
desc temp_table; -- describe is used to descirbe tables only.


-- ________________________________________________
/*
ALTER TABLE table_name  
ADD new_column_name column_definition  
[ FIRST | AFTER column_name ]; 
*/

alter table temp_table
add name text
after col1,-- after or first col_name,
add surname text
after name;

select * from temp_table;

alter table temp_table
modify name text
after col3;

alter table temp_table
drop column col3;

alter table temp_table
change column surname last_name
text;

-- rename table
alter table temp_table
rename to temp_tab;