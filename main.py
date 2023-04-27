import mysql.connector
import db_functions
import os
import hide

os.system('cls')


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
    user = input("What are you here for today? (depsoit, withdrawal, create account, balance, close account, modify account): ")
    if user.lower() == "balance":
        db_functions.balance()
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
        db_functions.deposit()
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
        db_functions.withdraw()
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
        db_functions.create_account()
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
        db_functions.close_account()
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
        db_functions.mod_account()
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
print("Thank you for your time. :)")






cursor.close()
connection.close()