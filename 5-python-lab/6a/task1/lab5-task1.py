def sing_up(**kwargs):
    if check_is_password_correct(kwargs[userName]):
        print("You create new account!")

def check_is_password_correct(pas):
    if len(pas) > 8 or len(pas) < 4:
        print("Password must be at least 8 characters long!")
        return False
    else:
        for letter in password:
            if letter.isalpha() or letter.isupper() or letter.isdigit():
                return True
            else:
                print("Password is not correct.")
                return False


userName = str(input("Enter your username: "))
password = str(input("Enter your password: "))

data = {userName: password}
sing_up(**data)