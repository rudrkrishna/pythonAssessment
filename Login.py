import csv

from AdminLogin import AdminLogin
from UserLogin import UserLogin
from jproperties import Properties




class Login:


    def login(self):

        print("******Welcome to BookMyShow*******")
        userID= input("User: ")
        password= input("Password: ")


        if userID == "Admin":
            self.adminpasswordValidation(userID, password)
            AdminLogin().adminLogin()
        else:
            self.userpasswordvalidation(userID, password)
            UserLogin().userLogin(userID)

    def adminpasswordValidation(self, userID, password):
        configs = Properties()
        with open('credentials.properties', 'rb') as read_prop:
            configs.load(read_prop)
        prop_view = configs.items()

        creddict={}
        for item in prop_view:
            creddict[str(item[0])] = str(item[1].data)
            if str(item[0]) == userID:
                if str(item[1].data) == password:
                    print("Login Successful")
                else:
                    print("Invalid credentials")
                    self.login()
        if userID not in creddict.keys():
            print("Invalid credentials")
            self.login()

    def userpasswordvalidation(self, userid, password):
        with open('userdetails.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if str(row[0]) == str(userid) and str(row[4]) == str(password):
                    print("Login Successful")
                    return True

            print("Invalid Credentials")
            self.login()




