import csvReaderCode


class RegisterNewAccount:

    def registeration(self):
        print("****Create new Account*****")
        name = input("Name: ")
        email = input("Email: ")
        phnno = input("Phone: ")
        age = int(input("Age: "))
        password = input("Password: ")
        user=[name, email, phnno, age, password]
        csvReaderCode.addUsers(user)



