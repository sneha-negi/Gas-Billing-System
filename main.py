import utils.py
import setup_db.py
import mysql.connector

connectDatabase()
print("Connected")
create_table_customers()
create_table_bills()
create_table_users()
ans= 'y'
while ans=='y':
    print("-"*30)
    print("Choose Operations:")
    print("Press 1- Add user.")
    print("Press 2- Login.")
    print("Press 3- Quit.")
    print("-"*30)
    opt1=int(input("Enter your choice:"))
    if opt1==1:
        add_user()
        ans=input('Would you like to continue? (y/n)')
        
    elif opt1==2:
        ans1="y"
        if login():
            while ans1=='y':
                if A:
                    print("*"*40)
                    print("Press 1- Show details of all customers.")
                    print("Press 2- Show details of a specific customer.")
                    print("Press 3- Display all Bills.")
                    print("Press 4- Quit.")
                    print("*"*40)
                    opt2=int(input("Enter your choice:"))
                    if opt2==1:
                        display_customers()
                        ans1=input('Would you like to continue? (y/n)')
                        if ans1=='n':
                            ans='n'
                    elif opt2==2:
                        display_customer()
                        ans1=input('Would you like to continue? (y/n)')
                        if ans1=='n':
                            ans='n'
                    elif opt2==3:
                        display_bills()
                        ans1=input('Would you like to continue? (y/n)')
                        if ans1=='n':
                            ans='n'
                    elif opt2==4:
                        ans='n'
                        ans1='n'
                    else:
                        print("Unable to process. Please try again.")
                        ans1=input('Would you like to continue? (y/n)')
                        if ans1=='n':
                            ans='n'
                else:
                    print("*"*40)
                    print("Press 1- Add a new customer.")
                    print("Press 2- Generate Bill.")
                    print("Press 3- Mark Bill as Paid.")
                    print("Press 4- Quit.")
                    opt3=int(input("Enter your choice:"))
                    if opt3==1:
                        add_customer()
                        ans1=input('Would you like to continue? (y/n)')
                        if ans1=='n':
                            ans='n'
                    elif opt3==2:
                        generate_bill()
                        ans1=input('Would you like to continue? (y/n)')
                        if ans1=='n':
                            ans='n'
                    elif opt3==3:
                        mark_bill_as_paid()
                        ans1=input('Would you like to continue? (y/n)')
                        if ans1=='n':
                            ans='n'
                    elif opt3==4:
                        ans='n'
                        ans1='n'
                    
                    else:
                        print("Unable to process. Please try again.")
                        ans1=input('Would you like to continue? (y/n)')
                        if ans1=='n':
                            ans='n'
    elif opt1==3:
        break
    else:
        print("Unable to process. Please try again.")
        ans=input('Would you like to continue? (y/n)')
