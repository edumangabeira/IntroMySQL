import psycopg2


try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the Database")
    print(e)
conn.set_session(autocommit=True)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS transactions2 (id int, \
    customer text, cashier_id int, year int)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS albums_sold (album_id int, \
    transaction_id int, name text)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS employees (id int, \
    name text)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS sales (transaction_id int, \
    amt_spent float)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO transactions2 (id, customer, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)",
                (1, "Amanda", 1, 2000))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO transactions2 (id, customer, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)",
                (2, "Toby", 1, 2000))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO transactions2 (id, customer, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)",
                (3, "Max", 2, 2018))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (1, 1, "Rubber Soul"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (2, 1, "Let It Be"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (3, 2, "My Generation"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (4, 3, "Meet the Beatles"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (5, 3, "Help!"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO employees (id, name) \
                 VALUES (%s, %s)",
                (1, "Sam"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO employees (id, name) \
                 VALUES (%s, %s)",
                (2, "Bob"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO sales (transaction_id, amt_spent) \
                 VALUES (%s, %s)",
                (1, 40))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO sales (transaction_id, amt_spent) \
                 VALUES (%s, %s)",
                (2, 19))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO sales (transaction_id, amt_spent) \
                 VALUES (%s, %s)",
                (3, 45))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

print("Table: transactions2\n")
try:
    cur.execute("SELECT * FROM transactions2;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

print("\nTable: albums_sold\n")
try:
    cur.execute("SELECT * FROM albums_sold;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

print("\nTable: employees\n")
try:
    cur.execute("SELECT * FROM employees;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

print("\nTable: sales\n")
try:
    cur.execute("SELECT * FROM sales;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

try:
    cur.execute("SELECT * FROM transactions2 a JOIN albums_sold b ON \
    a.id = b.transaction_id \
    JOIN employees c ON \
    a.cashier_id = c.id \
    JOIN sales d ON \
    a.id = d.transaction_id")


except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

# TO-DO: Create all tables
try:
    cur.execute("CREATE TABLE IF NOT EXISTS transactions(id int, customer text, \
    cashier_id int, year int, amt_spent float)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)


# Insert data into all tables

try:
    cur.execute("INSERT INTO transactions (id, customer, cashier_id, \
    year, amt_spent) \
                 VALUES (%s, %s, %s, %s, %s)",
                (1, 'Amanda', 1, 2000, 40))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO transactions (id, customer, cashier_id, \
    year, amt_spent) \
                 VALUES (%s, %s, %s, %s, %s)",
                (2, 'Toby', 1, 2000, 19))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO transactions (id, customer, cashier_id, \
    year, amt_spent) \
                 VALUES (%s, %s, %s, %s, %s)",
                (3, 'Max', 2, 2018, 45))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("SELECT id, customer, amt_spent FROM transactions")

except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

try:
    cur.execute("CREATE TABLE IF NOT EXISTS cashier_sales(transaction_id int \
    , name text, cashier_id int, amt_spent float)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)


# Insert into all tables

try:
    cur.execute("INSERT INTO cashier_sales (transaction_id, name, \
    cashier_id, amt_spent) \
                 VALUES (%s, %s, %s, %s)",
                (1, 'Sam', 1, 40))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO cashier_sales (transaction_id, name, \
    cashier_id, amt_spent) \
                 VALUES (%s, %s, %s, %s)",
                (2, 'Sam', 1, 19))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO cashier_sales (transaction_id, name, \
    cashier_id, amt_spent) \
                 VALUES (%s, %s, %s, %s)",
                (3, 'Bob', 2, 45))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("SELECT name, SUM(amt_spent) FROM cashier_sales \
    GROUP BY name")

except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

try:
    cur.execute("DROP table transactions2")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table albums_sold")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table employees")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table sales")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table transactions")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table cashier_sales")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)

cur.close()
conn.close()
