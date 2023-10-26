import psycopg2

db = {
    'dbname' : 'Your database name',
    'host' : 'Your host name',
    'user' : 'Database user name',
    'password' : 'postgresql password',
    'port' : 'postgresql port'

}

print('''We have different categories for your expenses and are given below, kindly select from the given category with correct category name to store the expenses, Categories are :- 
1) outside food
2) transportation
3) house_rent
4) electricity_bill
5) installment
6) medical_bill
7) grocery
8) gas_bill
9) selfcare
10) fuel''')

link = psycopg2.connect(**db)
cur = link.cursor()

def user_name(name):
    user_name = name
    command_user = ''' INSERT INTO users (user_name)
    VALUES(%s)
    '''
    cur.execute(command_user, (user_name,))

    link.commit()
    
def salaries(name, earning):
    user_salary = earning
    cur.execute("SELECT user_id FROM users WHERE user_name = %s", (name,))
    user_id = cur.fetchone()[0]
    command_salary = '''INSERT INTO salaries(user_id, salary)
    VALUES(%s, %s)'''

    cur.execute(command_salary, (user_id, user_salary))

    link.commit()
    
def expenditure(name, spend, money):
    amount = money
    cur.execute("SELECT user_id FROM users WHERE user_name = %s", (name,))
    user_id = cur.fetchone()[0]

    cur.execute("SELECT expense_id FROM expense_types WHERE expense_type = %s", (spend,))
    expense_id = cur.fetchone()[0]

    command_expenditure = '''INSERT INTO expense(user_id, expense_id, amount)
    VALUES(%s, %s, %s)'''
    cur.execute(command_expenditure, (user_id, expense_id, amount))

    link.commit()
    
def spent(name):
    username = name
    cur.execute("SELECT user_name FROM users where user_name = %s", (username,))
    command_spent= '''SELECT DISTINCT u.user_name , u.user_id, s.salary, e.expense_type, ex.amount
    FROM users AS u
    JOIN expense AS ex ON u.user_id = ex.user_id
    JOIN salaries AS s ON u.user_id = s.user_id
    JOIN expense_types AS e ON ex.expense_id = e.expense_id
    WHERE user_name = %s'''

    cur.execute(command_spent, (username,))

    spent_data = cur.fetchall()
    for r in spent_data:
        print(r)

authenticate = input("Are you already a user yes/no ? :- ")

if authenticate.lower() == 'no' or authenticate == '0':
    name = input("Enter your unique user name :- ")
    earning = int(input("Enter your salary or earning :- "))
    spend = input("Enter your expenditure name from the above given list :- ")
    money = int(input("Now, please tell the amount you spent on your selected expenditure name :- "))

    user_name(name)
    salaries(name, earning)
    expenditure(name, spend, money)
    spent(name)
else:
    a = input("Enter your already registered unique user name :- ")
    spend = input("Enter your expenditure name from the above given list :- ")
    money = int(input("Now, please tell the amount you spent on your selected expenditure name :- "))
    print("Greetings User, Here are all your Expenses till now! ")
    expenditure(a, spend, money)
    spent(a)

cur.close()
link.close()







