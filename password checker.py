valid_password = False
contains_digit= False

while not valid_password: 
    new_password = input("Please enter your new password: ")
    new_password2 = input("Please enter your new password again: ")

    if new_password != new_password2:
        print("The passwords don't match up.")
        continue
    elif len(new_password) < 8:
        print("Your password must be longer")
        continue
    elif new_password.upper() == new_password or new_password.lower() == new_password:
        print("Your password must contain at least one lowercase and uppercase letter")
        continue 
    else:
        print("Password Accepted!")
        valid_password = True
