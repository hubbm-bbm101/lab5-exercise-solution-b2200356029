def v_email(x):
    if "@" in x and "." in x:
        return True
    else:
        return False

email = input("please enter an e-mail: ")
if v_email(email):
    print("valid e-mail")
else:
    print("not a valid e-mail")
