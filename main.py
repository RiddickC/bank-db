import mysql.connector
import db_functions
import os
import hide

os.system('cls')

hasAccount = None
acID = None
acPin = None
account = None
user1 = ""


connection = mysql.connector.connect(
    user = 'root',
    database = 'bankdatabase',
    password = hide.password
)

cursor = connection.cursor()

print("-----WELCOME TO THEE BANK-----")
print("-----If you wish to exit-----")
print("---------Type (exit)---------")

while True: 
    user0 = input("Do you have an account with us? (yes/no): ")

    if user0.lower() == 'no':
        while True:

            user1 = input("Welcome New User. Would you like to make an account? (Yes/No): ")
            if user1.lower() == 'yes':
                account = db_functions.create_account()
                for item in account:
                    acID = item[0]
                    acPin = item[1]
                hasAccount = False
                break
            elif user1.lower() == 'no':
                break
            else:
                print("Try again.")
        print()
        if user1.lower() == 'no':
            break
    elif user0.lower() == 'yes':
        account = db_functions.getAccount()
        for item in account:
            acID = item[0]
            acPin = item[1]
        hasAccount = True
        break
    elif user0.lower() == 'exit':
        break
    else:
        print("Try again.")

while True:
    if user0.lower() == 'exit':
        break
    if user1.lower() == 'no':
        break
    if hasAccount == True:
        if db_functions.check_admin(acID, acPin):
            db_functions.main_admin_or_new(acID,acPin)
        else:
            db_functions.main_user(acID,acPin)
    else:
        db_functions.main_admin_or_new(acID,acPin)
    break

print("Thank you for your time. :)")






cursor.close()
connection.close()