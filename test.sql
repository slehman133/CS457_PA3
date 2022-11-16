CREATE DATABASE CS457_PA3;
USE CS457_PA3;
CREATE TABLE Employee (id int, name varchar(10));
CREATE TABLE Sales (employeeID int, productID int);
select * 
from Employee E, Sales S 
where E.id = S.employeeID;
select * 
from Employee E inner join Sales S 
on E.id = S.employeeID;
select * 
from Employee E left outer join Sales S 
on E.id = S.employeeID;
.EXIT;