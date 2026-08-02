
def sign_up():
  print("Welcome to the sign-up page!")
  print("password should contain at least 8 characters, including at least one uppercase letter, one lowercase letter, and one number.")
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username.isalnum() and len(password) >= 8:
      print("Login successful!")
  else:
     print("Invalid username or password.")
    
sign_up()