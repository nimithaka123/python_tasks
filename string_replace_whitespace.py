
import re
input_string=input("enter a string:")
d = {' ' : '_', '_' : ' '}
print("After conversion")
print(re.sub(r'[ _]', lambda m: d[m[0]], input_string))


