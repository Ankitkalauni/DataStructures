/*
day 3

0. learned about the UI of workbench and mysql client command-line
1. create users for mysql server
2. Grant Privileges to the MySQL New User
3. play around with user and its manupilation, securities.
4. creating new user, modifying grants and changing passwords.
*/

create user if not exists public_user1@localhost identified by "public_user1";

-- grant all privileges on *.* to public_user@localhost;

grant create, select, insert on *.* to public_user1@localhost;

-- Sometimes, you want to flush all the privileges of a user account for changes occurs immediately, type the following command.
FLUSH PRIVILEGES;

select user from mysql.user;

show grants for public_user1@localhost;

-- drop user 'public_user1@localhost';
use mysql;

select user from mysql.user;

desc user;

select user, host, account_locked, password_expired from user;

-- see the current user
select user(); -- select current_user();

select user, host, db, command from information_schema.processlist;

-- update user password
use mysql;
select version();

-- update user set authentication_string = password('root') where user = 'public_user1' and host = 'localhost';
-- the above comment code not work but the below code works in verison 8
set password for "public_user"@"ankit" = "root";
alter user public_user1@localhost identified by 'root';

show databases;
use movies;
show schemas;
show databases like '%schema';
SELECT schema_name FROM information_schema.schemata;  -- same as show databases;
SELECT schema_name FROM information_schema.schemata WHERE schema_name LIKE 's%';  
