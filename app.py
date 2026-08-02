
def sign_up():
  username = input("Enter your username: ")
  password = int(input("Enter your password: "))
  if username.isalnum():
      print("Login successful!")
      
  else:
     print("Invalid username or password.")
    
sign_up()