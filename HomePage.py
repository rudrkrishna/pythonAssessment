import csv
import RegisterNewAccount
from Login import Login
from RegisterNewAccount import RegisterNewAccount


class HomePage:
    flag = True
    while flag:
        print("******Welcome to BookMyShow*******")
        print("1. Login")
        print("2. Register new account")
        print("3. Exit")
        # fileVariable = open('booking_file.csv', 'r+')
        # fileVariable.truncate(0)
        selectOption = int(input("Enter: "))

        match selectOption:
            case 1:
                Login().login()
            case 2:
                RegisterNewAccount().registeration()
            case 3:
                flag = False



