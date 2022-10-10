import random
list_shuffle=[]


string1=input("enter a string:")
list_string=list(string1)
a =[]
while True:
    random.shuffle(list_string)
    x=''.join(list_string)
    if x not in list_shuffle:
        list_shuffle.append(x)
    else:
        break
print(list_shuffle)