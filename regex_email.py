import re
# str1="nimi@gmail.com"
input_email=input("enter a email id:")
email_before=re.split("@",input_email)
print("email part before @ is:")
print(email_before[0])
print("email part till @ is:")
print(email_before[0]+"@")

