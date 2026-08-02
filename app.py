def login():
    # Function to handle user login
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Here you would typically check the username and password against a database
    if authenticate_user(username, password):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False