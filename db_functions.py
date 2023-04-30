import mysql.connector
import random
import hide
import os


connection = mysql.connector.connect(
    user = 'root',
    database = 'bankdatabase',
    password = hide.password
)
cursor = connection.cursor()

def getAccount():
    os.system('cls')
    acID = int(input("Enter your Account ID: "))
    acPin = int(input("Enter your Account Pin Number: "))
    cursor.execute(f'SELECT * FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}')

    return cursor
    
def balance(acID, acPin):
    os.system('cls')
    cursor.execute(f'SELECT bal FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}')
    for item in cursor:
        print(f'Balance: ${item[0]}')
    print()

def deposit(acID, acPin):
    os.system('cls')
    while True:
        amount = int(input("How much would you like to deposit into your account?: "))
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

def withdraw(acID, acPin):
    os.system('cls')
    cursor.execute(f'SELECT bal FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}')
    for item in cursor:
        bal = item[0]
    while True:
        amount = int(input("How much would you like to withdraw from your account?: "))
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
    os.system('cls')
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

def close_account(acID, acPin):
    os.system('cls')
    while True:
        user = input("Are you sure you want to close this account? (yes/no): ")
        if user.lower() == 'yes':
            cursor.execute(f"DELETE FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}")
            print("Your account has been deleted and can no longer be accessed.")
            connection.commit()
            break
        elif user.lower() == 'no':
            print("Your account was not closed.")
            break
        else:
            print("Try again.")

def mod_account(acID):
    os.system('cls')
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
    print("Account has been modified.")\
    
def check_admin(acID, acPin):
    admin = False
    cursor.execute(f'SELECT admin FROM bankInformation WHERE acID = {acID} AND acPin = {acPin}')
    for item in cursor:
        if item[0] == 'yes':
            admin = True
        else:
            admin = False
        
    return admin
def main_admin_or_new(acID,acPin):
    os.system('cls')
    while True:
        user = input("What are you here for today? (depsoit, withdrawal, balance, create account, close account, modify account): ")
        if user.lower() == "balance":
            balance(acID,acPin)
            while True:
                user2 = input("Would you like to exit? (Yes/No): ")
                if user2.lower() == "yes":
                    break
                elif user2.lower() == "no":
                    break
                else:
                    print("Please try again.")
            if user2.lower() == "yes":
                break
        elif user.lower() == "deposit":
            deposit(acID,acPin)
            while True:
                user2 = input("Would you like to exit? (Yes/No): ")
                if user2.lower() == "yes":
                    break
                elif user2.lower() == "no":
                    break
                else:
                    print("Please try again.")
            if user2.lower() == "yes":
                break
        elif user.lower() == "withdrawal":
            withdraw(acID,acPin)
            while True:
                user2 = input("Would you like to exit? (Yes/No): ")
                if user2.lower() == "yes":
                    break
                elif user2.lower() == "no":
                    break
                else:
                    print("Please try again.")
            if user2.lower() == "yes":
                break
        elif user.lower() == "create account":
            create_account()
            while True:
                user2 = input("Would you like to exit? (Yes/No): ")
                if user2.lower() == "yes":
                    break
                elif user2.lower() == "no":
                    break
                else:
                    print("Please try again.")
            if user2.lower() == "yes":
                break
        elif user.lower() == "close account":
            close_account(acID,acPin)
            while True:
                user2 = input("Would you like to exit? (Yes/No): ")
                if user2.lower() == "yes":
                    break
                elif user2.lower() == "no":
                    break
                else:
                    print("Please try again.")
            if user2.lower() == "yes":
                break
        elif user.lower() == "modify account":
            mod_account(acID,acPin)
            while True:
                user2 = input("Would you like to exit? (Yes/No): ")
                if user2.lower() == "yes":
                    break
                elif user2.lower() == "no":
                    break
                else:
                    print("Please try again.")
            if user2.lower() == "yes":
                break
        elif user.lower() == "exit":
            break
        else:
            print("Try again.")

def main_user(acID,acPin):
    os.system('cls')
    while True:
        user = input("What are you here for today? (depsoit, withdrawal, balance): ")
        if user.lower() == "balance":
            balance(acID,acPin)
            while True:
                user2 = input("Would you like to exit? (Yes/No): ")
                if user2.lower() == "yes":
                    break
                elif user2.lower() == "no":
                    break
                else:
                    print("Please try again.")
            if user2.lower() == "yes":
                break
        elif user.lower() == "deposit":
            deposit(acID,acPin)
            while True:
                user2 = input("Would you like to exit? (Yes/No): ")
                if user2.lower() == "yes":
                    break
                elif user2.lower() == "no":
                    break
                else:
                    print("Please try again.")
            if user2.lower() == "yes":
                break
        elif user.lower() == "withdrawal":
            withdraw(acID,acPin)
            while True:
                user2 = input("Would you like to exit? (Yes/No): ")
                if user2.lower() == "yes":
                    break
                elif user2.lower() == "no":
                    break
                else:
                    print("Please try again.")
            if user2.lower() == "yes":
                break
        elif user.lower() == "exit":
            break
        else:
            print("Try again.")
            
