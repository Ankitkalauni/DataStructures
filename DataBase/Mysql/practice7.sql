-- How to Fix a Corrupted Table in MySQL?
-- The following is the syntax to repair a corrupted table in MySQL:

/*
REPAIR [NO_WRITE_TO_BINLOG | LOCAL]  
    TABLE tbl_name [, tbl_name] ...  
    [QUICK] [EXTENDED] [USE_FRM]
*/
use movies;

CREATE TABLE vehicle (  
    vehicle_no VARCHAR(18) PRIMARY KEY,  
    model_name VARCHAR(45),  
    cost_price DECIMAL(10,2 ),  
    sell_price DECIMAL(10,2)  
);

INSERT INTO vehicle (vehicle_no, model_name, cost_price, sell_price) VALUES('S2001', 'Scorpio', 950000, 1000000),  
('M3000', 'Mercedes', 2500000, 3000000),  
('R0001', 'Rolls Royas', 75000000, 85000000); 

SELECT * FROM vehicle;

SELECT table_name, engine   
FROM information_schema.tables   
WHERE table_name = 'vehicle';

REPAIR TABLE vehicle;  -- error print

ALTER TABLE vehicle ENGINE = 'MyISAM';  
-- Now, use the repair table query   
REPAIR TABLE vehicle;


-- add and delete column 
/*
ALTER TABLE table_name   
    ADD COLUMN column_name column_definition [FIRST|AFTER existing_column];
*/

alter table movies_info -- add new col
add column temp_col int not null;

alter table movies_info -- rename col
change column temp_col temp_col_new_name int not null;

alter table movies_info -- drop col
drop column temp_col_new_name;

-- 			show columns
-- 			extended (optional) to see hidden columns also
-- The FULL is also an optional keyword to display
-- the column information, including collation, comments
-- and the privileges we have for each column.

show columns from movies.movies_info;
show extended columns from movies.movies_info;
show full columns from movies.movies_info;

-- mysql view

/*
MySQL allows us to create a view in mainly two ways:

MySQL Command line client
MySQL Workbench
*/

create view temp as -- or "replace" the existing view
select * from movies_info; -- where condition

drop view if exists temp;

/*
ALTER VIEW view_name AS    
SELECT columns    
FROM table    
WHERE conditions;  
*/

/*
CREATE VIEW Trainer       
AS SELECT c.course_name, c.trainer, t.email       
FROM courses c, contact t   
WHERE c.id = t.id;  
*/
