# expense-tracker
It is an expense tracker built using python and PostgreSQL along with using a python library psycopg2.

It includes around 10 different expense types such as "outside food", "medical bill" , "grocery" and much more.


You first need to create a database and then the given tables along with their field/columns :-

TABLE NAME :- COLUMNS 
1) users = user_id(pk), user_name
2) salaries = user_id(fk,pk), salary
3) expense_types = expense_id(pk), expense_type
4) expense = user_id(fk,pk), expense_id(fk,pk), amount

fk = foreign key
pk = primary key

Also, you need to keep in mind about the constraints and data type while creating the tables. for ex:- we can use "VARCHAR(255) to store the username so that user can make username using different characters, another example will be using combination of "user_id" and "expense_id" as primary key in the "expense" table which ensures referential integrity as they are foreign key as well and also removes our need to create a separate primary key for "expense" table. Also using both of them as primary key, they ensure efficient use of "JOIN" clause to get data from users,expense_types as well as expense table.


**Here's the screenshot of the working of the Expense Tracker**


![expense tracker , NO EXPENSE](https://github.com/ujjwal717/expense-tracker/assets/93403224/38dc3e9e-583c-49f0-9e6c-df4e756d7d74)



