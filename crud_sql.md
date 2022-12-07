3. producers table
select * from producers --- displays all the rows in producers table

##update operation

update producers set prod_category="sports" ---updates the product category to sports where where trans_id=22212043

##delete operation

delete from producers ---deletes a row where trans_id=22212045 where trans_id=22212045

truncate table producers; ---deletes all the data from producers table but not structure

4. Locations table:
select * from locations ---displays all the data from locations table

select postal_code from locations where city = "hyderabad"; --displays postal_code wherecity is hyderabad

##update operation

update locations set city="warangal" where cust_id=1004 ---updates city column value to warangal where cust_id=1004

##delete operation

delete from customers where cust_id=1005 ----deletes a row where cust_id=1005

truncate table locations; ---deletes all the data from locations table but not structure
