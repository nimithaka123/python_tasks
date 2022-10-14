from ast import pattern
import re


mob_num=input("enter your mobile number:")
pattern=re.compile("(0|91)?[-\s]?[6-9][0-9]{9}")

if pattern.match(mob_num):
    print("valid number")
else:
    print("in valid")