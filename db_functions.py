import mysql.connector
import random


connection = mysql.connector.connect(
    user = 'root',
    database = 'bankdatabase',
    password = 'Bivl*9876'
)
cursor = connection.cursor()

def balance():
    
    acID = int(input("Enter your Account ID: "))
    acPin = int(input("Enter your Account Pin Number: "))
        
    cursor.execute(f'SELECT bal FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}')
    for item in cursor:
        print(f'Balance: ${item[0]}')
    print()

def deposit():
    acID = int(input("Enter your Account ID: "))
    acPin = int(input("Enter your Account Pin Number: "))
    while True:
        amount = int(input("How much would you like to deposit into your account? "))
        if amount < 0:
            print("Can't deposit nothing.")
        else:
            break
    cursor.execute(f'UPDATE bankInformation SET bal = bal + {amount} WHERE acID = {acID} AND acPin = {acPin}')
    cursor.execute(f'SELECT bal FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}')
    for item in cursor:
        print(f'Successfully deposited ${amount}.')
        print(f'Balance: ${item[0]}')
    print()
    connection.commit()

def withdraw():
    acID = int(input("Enter your Account ID: "))
    acPin = int(input("Enter your Account Pin Number: "))
    cursor.execute(f'SELECT bal FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}')
    for item in cursor:
        bal = item[0]
    while True:
        amount = int(input("How much would you like to withdraw from your account? "))
        if amount > bal:
            print("You cannot withdraw that amount. Please try again.")
        else:
            break

    cursor.execute(f'UPDATE bankInformation SET bal = bal - {amount} WHERE acID = {acID} AND acPin = {acPin}')
    cursor.execute(f'SELECT bal FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}')
    for item in cursor:
        print(f'Successfully widthdrew ${amount}.')
        print(f'Balance: ${item[0]}')
    print()
    connection.commit()

def create_account():
    acName = input("What is your name for the account?: ")
    acAddress = input("What is your address for the account?: ")
    acDOB = input("What is your date of birth for the account? (mm/dd/yyyy): ")
    while True:
        acPin = int(input("Enter the pin you would like to use (4 digits): "))
        if len(str(acPin)) > 4 or len(str(acPin)) < 4:
            print("Not a good enough pin. Please try again.")
        else:
            break
    while True:
        amountTemp = input("Would you like to deposit an initial value? (Yes/No): ")
        if amountTemp.lower() == "yes":
            amount = int(input("How much would you like to deposit?: "))
            break
        elif amountTemp.lower() == "no":
            amount = 0
            break
        else:
            print("Please try again.")
    while True:
        acID = random.randint(10000, 99999)
        check = cursor.execute(f'SELECT bal FROM bankInformation WHERE acID = {acID}')
        if(check is None):
            break
        else: 
            continue
    cursor.execute(f"INSERT INTO bankInformation (acID, acPin, bal, name, address, dob) VALUES ({acID}, {acPin}, {amount}, {acName}, {acAddress}, {acDOB})")
    print()

def close_account():
    acID = int(input("Enter the Account ID you want to close: "))
    acPin = int(input("Enter the Account Pin Number you want to close: "))
    cursor.execute(f"DELETE FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}")
    print("Your account has been deleted and can no longer be accessed.")

def mod_account():
    acID = int(input("Enter the ID of the account you want to modify: "))
    acPin = int(input("Enter the Pin number of the account you want to modify: "))
    while True:
        user = input("What would u like to modify about the account? (Pin number, Name, Address, Date of Birth): ")
        if user.lower() == "pin number":
            while True:
                userPin = int(input("Enter the new pin you would like to use (4 digits): "))
                if len(str(userPin)) > 4 or len(str(userPin)) < 4:
                    print("Not a good enough pin. Please try again.")
                else:
                    break
            cursor.execute(f'UPDATE bankInformation SET acPin = {userPin} WHERE acID = {acID}')
            break
        elif user.lower() == "name":
            userName = input("What would you like the new name to be?: ")
            cursor.execute(f'UPDATE bankInformation SET name = {userName} WHERE acID = {acID}')
            break
        elif user.lower() == "address":
            userAddr = input("What would you like the new address to be?: ")
            cursor.execute(f'UPDATE bankInformation SET address = {userAddr} WHERE acID = {acID}')
            break
        elif user.lower() == "date of birth":
            userDOB = input("What would you like the new Date of Birth to be?: ")
            cursor.execute(f'UPDATE bankInformation SET dob = {userDOB} WHERE acID = {acID}')
            break
        else:
            print("Please try again.")
    print("Account has been modified.")
    
