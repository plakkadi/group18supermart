#########CRUD OPERATIONS ON DATABASE#########

1) ORDERS TABLE:

creating is done in create_sql.md file

select * from orders; -- displays all the rows of orders table

select * from orders where cust_id=1001; --displays all column values where cust_id=1001

select * from orders where units_sold > 9; --displays all column values where units_sold is greater than 9;

select purch_date from orders where cust_id=1005; --displays purch_date from order where cust_id is 1005;

##update operation

update orders
set units_sold=8 where cust_id=1001; ----updates order table of units_sold from 3to8 where cust_id=1001

##delete operation

delete from orders where trans_id=22212041; ---deletes the row where trans_id=22212041;

##truncate operation

truncate table orders; --deletes data from the orders table but not the structure

2) customers table

select * from customers; ---displays all data from customers table

select cust_name where cust_id = 1003; --displays the cust_name using cust_id

##update operation

update customers set cust_name="vikas", contact_no = 9701619073 where cust_id=1004; ---updates cust_name and contact_no at cust_id=1004

##delete operation

delete from customers where cust_id=1005; ---deletes the entire row where cust_id=1005

truncate table customers; ---deltes data from customer table but not the structure

3) producers table
select * from producers --- displays all the rows in producers table

##update operation

update producers set prod_category="sports" ---updates the product category to sports where where trans_id=22212043

##delete operation

delete from producers ---deletes a row where trans_id=22212045 where trans_id=22212045

truncate table producers; ---deletes all the data from producers table but not structure

4) Locations table:
select * from locations ---displays all the data from locations table

select postal_code from locations where city = "hyderabad"; --displays postal_code wherecity is hyderabad

##update operation

update locations set city="warangal" where cust_id=1004 ---updates city column value to warangal where cust_id=1004

##delete operation

delete from customers where cust_id=1005 ----deletes a row where cust_id=1005

truncate table locations; ---deletes all the data from locations table but not structure
