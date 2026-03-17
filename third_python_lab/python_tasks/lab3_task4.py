logins = []
passwords = []

while True:
    login = str(input("Enter your login: "))

    if login.upper() == "STOP":
        break

    elif login == "":
        print("Field LOGIN is empty!")

    else:
        logins.append(login)
        password = str(input("Enter your password: "))
        passwords.append(password)

loginAndPasswordDict = {}
for i, login in enumerate(logins):
    loginAndPasswordDict[login] = passwords[i]

print("\t LOGINS: ", *logins)
print("\t PASSWORDS: ", *passwords)
for login, password in loginAndPasswordDict.items():
    print(f" login: {login}, password: {password}")
