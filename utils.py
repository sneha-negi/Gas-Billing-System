import mysql.connector

def login():
    global A
    print("-"*30)
    print("Gas Billing System")
    print("-"*30)
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    query = "SELECT * FROM users WHERE username=%s and password=%s"
    vals = (username, password)
    mycursor = mydb.cursor()
    mycursor.execute(query, vals)
    result = mycursor.fetchall()
    print("-"*50)
    A=False
    if len(result)==0:
        print("Invalid username and/or password")
        print("-"*50)
        return False
    elif username=="gas auth" and password=="abc123":
        print("Access Granted to Authority.")
        print("-"*50)
        A=True
        return True
    else:
        print("Access Granted.")
        print("-"*50)
        return True
    
def add_user():
    mycursor = mydb.cursor()
    username = input("Enter the username : ")
    password = input("Enter the password : ")
    vals = (username, password)
    query = "INSERT INTO users (username, password) \
         VALUES (%s, %s)"
    mycursor.execute(query, vals)
    mydb.commit()
    query = "SELECT * FROM users WHERE username=%s"
    mycursor.execute(query,(username,))
    results = mycursor.fetchall()
    for res in results:
        if res[1]==username:
            print("User id",res[0])

def add_customer():
    mycursor = mydb.cursor()
    customer_name = input("Enter the customer's name :")
    address = input("Enter the customer's address :")
    phone = input("Enter the customer's phone number : ")
    email_id = input("Enter the customer's email id : ")
    vals = (customer_name, address, phone, email_id)
    query = "INSERT INTO customers (customer_name, address, phone, email_id) \
         VALUES (%s, %s, %s, %s)"
    mycursor.execute(query, vals)
    mydb.commit()
    query = "SELECT * FROM customers WHERE phone=%s"
    mycursor.execute(query,(phone,))
    results = mycursor.fetchall()
    for res in results:
        if res[3]==phone:
            print("Customer id",res[0])
    

def generate_bill():
    mycursor = mydb.cursor()
    customer_id = input("Enter the customer id : ")
    bill_startdate = input("Enter the billing start date : ")
    bill_enddate = input("Enter the billing end date : ")
    curr_units_on_meter = int(input("Enter the current units displayed on the meter: "))
    prev_units_on_meter = int(input("Enter the previously displayed units on the meter: "))
    number_of_units = curr_units_on_meter - prev_units_on_meter
    bill_amount = 0
    curr_units = number_of_units
    if curr_units>200:
        curr_units-=200
        bill_amount+=400
    else:
        bill_amount+=2*curr_units
        curr_units=0
    
    if curr_units>300:
        curr_units-= 300
        bill_amount+=1200
    else:
        bill_amount+=4*curr_units
        curr_units=0
    
    bill_amount+=8*curr_units
    bill_paid = "No"
    vals = (customer_id, bill_startdate, bill_enddate, number_of_units, bill_amount, bill_paid)
    query = "INSERT INTO bills (customer_id, bill_startdate, bill_enddate,\
                 number_of_units, bill_amount, bill_paid) \
         VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, vals)
    mydb.commit()
    query = "SELECT * FROM bills WHERE customer_id=%s"
    mycursor.execute(query,(customer_id,))
    results = mycursor.fetchall()
    for res in results:
        if res[1]==customer_id:
            print("Bill id",res[0])

def display_customers():
    mycursor = mydb.cursor()
    query = "SELECT * FROM customers"
    mycursor.execute(query)
    results = mycursor.fetchall()
    s=" "
    print("Customer ID  Customer Name    Address                Phone      email ID") 
    for res in results:
        print(res[0],s*(13-len(str(res[0]))), res[1],s*(13-len(str(res[1]))),res[2],s*(19-len(str(res[2]))),\
                  res[3],s, res[4])
        
def display_customer():
    mycursor = mydb.cursor()
    query = "SELECT * FROM customers WHERE CUSTOMER_ID=%s"
    VAL=int(input("Enter Customer ID to be displayed:"))
    mycursor.execute(query,(VAL,))
    results = mycursor.fetchall()
    s=" "
    print("Customer ID  Customer Name    Address                Phone      email ID") 
    for res in results:
        if res[0]==VAL:
            print(res[0],s*(13-len(str(res[0]))), res[1],s*(13-len(str(res[1]))),res[2],s*(19-len(str(res[2]))),\
                  res[3],s, res[4])

def display_bills():
    mycursor = mydb.cursor()
    query = "SELECT * FROM bills"
    mycursor.execute(query)
    results = mycursor.fetchall()
    s=" "
    print("'Bill ID'  'Customer ID'  'Bill start date'  'Bill end date' 'number of units' 'bill amount' 'bill paid'") 
    for res in results:
        print(res[0],s*(11-len(str(res[0]))), res[1],s*(13-len(str(res[1]))),res[2],s*7,\
                  res[3],s*7, res[4],s*(15-len(str(res[4]))),res[5],s*(12-len(str(res[5]))), res[6])

def mark_bill_as_paid():
    mycursor = mydb.cursor()
    query = "UPDATE bills SET bill_paid = 'YES' WHERE bill_id=%s"
    bill_id = input("Enter the bill id of the bill to be marked as paid: ")
    vals = (bill_id,)
    mydb.commit()
    mycursor.execute(query, vals)
    results = mycursor.fetchall()
    for res in results:
        print(res)
    print("Bill paid.")
