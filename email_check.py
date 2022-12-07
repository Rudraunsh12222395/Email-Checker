import re
def emailcheck(email):
    if(re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}",email)):
        return True
    else:
        return False
def passwordcheck(password):
    if (re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&*])[a-zA-Z0-9@#$%^&*]{6,20}",password)):
        return True
    else:
        return False
email = input("Enter email: ")
password = input("Enter password: ")
if (emailcheck(email)==True):
    print("valid email")
else:
    print("invalid email")
if (passwordcheck(password)==True):
    print("valid password")
else:
    print("invalid password")                                   