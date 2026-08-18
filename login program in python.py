users = {"user1": "password1", "user2": "password2"}
def is_valid_user(username):
    #check if username exists in the user directory.
    return usrname in users

def check_password(username, password):
    #chec kif the provided passwoed matches the srored password ans validate them
    username = input("Enter your username: ")
    password = input("Enter your password: ")

def login():
    #prompt user for username and password and validate them
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if not is_valid_user(username):
        print("Username and/or password not found")
        return

    if check_password(username, password):
        print("Login sucessful!")
    else:
        print("Incorrect password.")

login()
            print("Login successful!")
