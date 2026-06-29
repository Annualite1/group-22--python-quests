# Initiated a variable called 'password' to store the password
password = "12345"
# Initiated a new variable to store a user-inputted password
user_password = input("Enter password to check: ")
# conditional statement to check if the password we have matches the one the user inserted, if it is correct, grant access if its not deny
if password == user_password:
	print ("Access Granted")
else: print("Acess Denied")
