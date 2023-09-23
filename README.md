# expense-tracker
It is an expense tracker built using python and PostgreSQL along with using a python library psycopg2.

You first need to create a database and then the given tables along with their field/columns :-

TABLE NAME :- COLUMNS 
1) users = user_id(pk), user_name
2) salaries = user_id(fk,pk), salary
3) expense_types = expense_id(pk), expense_type
4) expense = user_id(fk,pk), expense_id(fk,pk), amount

fk = foreign key
pk = primary key

