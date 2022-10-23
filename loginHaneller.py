import pandas as pd


class security:
    def __init__(self):
        self.users = pd.read_csv('users.csv')

    def register(self):

        username = input("Username:")
        password = input("Password:")

        self.users = self.users.append(pd.DataFrame([
        [username,password]], columns=['username','password']
        
        )).reset_index(drop=True)

        self.updateDB()

    def login(self):
        username = input("username:")
        user_password = input("password")

        try:
            a = self.users.loc[self.users['username'] == username]
            b = a['password'].iloc[0]

            

        except: 
            print("ERROR LOGIN")
            return 'User Not Found'
        
        if b == user_password:
            return True
        else: 
            return 'Wrong Password'


    def updateDB(self):
        self.users.to_csv('users.csv',index=False)

    def outputdf(self):
        print(self.users)


if __name__ == '__main__':
    sec = security()
    sec.login()