import mysql.connector
import db_functions
import os
import hide

os.system('cls')

hasAccount = None
acID = None
acPin = None
account = None


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
        account = db_functions.create_account()
        for item in account:
            acID = item[0]
            acPin = item[1]
        hasAccount = False
        break
    elif user0.lower() == 'yes':
        account = db_functions.getAccount()
        for item in account:
            acID = item[0]
            acPin = item[1]
        hasAccount = True
        break
    else:
        print("Try again.")



if hasAccount == True:
    if db_functions.check_admin(acID, acPin):
        db_functions.main_admin_or_new(acID,acPin)
    else:
        db_functions.main_user(acID,acPin)
elif hasAccount == False:
    db_functions.main_admin_or_new(acID,acPin)

print("Thank you for your time. :)")






cursor.close()
connection.close()