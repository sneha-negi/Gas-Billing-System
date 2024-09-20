
def connectDatabase():
    global mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sneha-125"
        )
    mycursor = mydb.cursor()
    try:
        query = "USE gas"
        mycursor.execute(query)
    except:
        query = "CREATE DATABASE gas"
        mycursor.execute(query)
        query = "USE gas"
        mycursor.execute(query)

def create_table_customers():
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS customers (customer_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, \
                        customer_name VARCHAR(255), address VARCHAR(255),\
                             phone VARCHAR(255), email_id VARCHAR(255))")
    print("Created Table Customers")

def create_table_bills():
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS bills (bill_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, \
                        customer_id VARCHAR(255), bill_startdate VARCHAR(255),\
                             bill_enddate VARCHAR(255), number_of_units VARCHAR(255),\
                                bill_amount VARCHAR(255), bill_paid VARCHAR(255))")
    print("Created Table Bills")

def create_table_users():
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        if x[0]=="users":
            print("Created Table Users")
            return
    mycursor.execute("CREATE TABLE users (user_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, \
                        username VARCHAR(255), password VARCHAR(255))")
    print("Created Table Users")
    mycursor.execute("INSERT INTO USERS(username, password) values('gas auth', 'abc123')")
    mydb.commit()
    print("Created Table Users")
