-- create database task22_23
-- use task22_23
-- create table users(
-- customers varchar(100),
-- prducts varchar(100),
-- employees varchar(100),
-- offices varchar(100),
-- orderdetails varchar(100)
-- )
-- ALTER TABLE users ADD COLUMN payments  VARCHAR(100);
-- ALTER TABLE users ADD COLUMN productlinesr VARCHAR(100);
-- ALTER TABLE users ADD COLUMN other_region_customer VARCHAR(100);
ALTER TABLE users ADD COLUMN orders VARCHAR(100);


insert into users(customers, prducts, employees, offices, orders, orderdetails, payments, productlinesr, other_region_customer) 
VALUES ("김범수", "낚시대", "주영광", "강남 신사옥", "구매", "3개", "카드지불", "민물낚시대", "양주");