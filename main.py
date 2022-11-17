import salesHandeller
import expenditureHandeller
import loginHaneller

sales = salesHandeller.sales()
expence = expenditureHandeller.expences()
users = loginHaneller.security()
loggedin = False

while loggedin != True: 
    loggedin = users.login_login()
    print(loggedin)

# sales.outputdf()

# sales.newsale()

# sales.outputdf()

# sales.plotlinegraph()

expence.outputdf()

expence.newexpence()

expence.outputdf()
# expence.plotlinegraph()

expence.editDB()

expence.outputdf()