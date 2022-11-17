import pandas as pd
import encryption

class security:
    def __init__(self):
        self.users = pd.read_csv('users.csv')

    def login_register(self):

        usr = input("Username:")
        pwd = input("Password:")
        if len(usr) <= 3:
            print("Error: Your password needs to be longer than 3 characters!")
        elif len(usr) >= 24:
            print("Error: Please have your password be shorter than 24 characters!")
        elif usr.find(" ") != -1: 
            print("Error: Usernames can not contain spaces!")
        if pwd.find(" ") != -1:
            print("Error: Passwords can not contain spaces!")
        else:
            if encryption.encrypt(usr,"usr"):
                encryption.encrypt(pwd, "psw")

    def login_login(self):
        usr = input("Username:")
        pwd = input("Password:")
        if encryption.decrypt(usr,"usr"):
            if encryption.decrypt(pwd, "psw"):
            # Call your menu function here example example.game_game()
            # The welcome is optional
                print("Welcome!")
                return True
            else:
                print("Failed")

		


    def updateDB(self):
        self.users.to_csv('users.csv',index=False)

    def outputdf(self):
        print(self.users)


if __name__ == '__main__':
    sec = security()
    sec.login_register()
    sec.login_login()