passwords = {
    "pass1" : "qwerty12345",
    "pass2" : "ytrewq54321"
}

userPassword = str(input())

if userPassword in passwords.values():
    print("Maksim Pyshynski")
else:
    print("The password is incorrect!")