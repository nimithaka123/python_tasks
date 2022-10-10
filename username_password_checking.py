user_name=input("enter your username:")
password=input("enter your password:")
recheck_username=input("enter your username once again:")
recheck_password=input("enter your password once again:")
if user_name==recheck_username and password==recheck_password:
    print("Your credential are correct")
else:
    print("Your credential are incorrect")