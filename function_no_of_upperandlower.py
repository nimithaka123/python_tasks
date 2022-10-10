def no_of_upperandlower(string1):
    u_count=0
    l_count=0
    for i in string1:
        if i.isupper():
            u_count=u_count+1
        if i.islower():
            l_count=l_count+1
    print("no of upper case letters:", u_count)
    print("no of lower case letters:", l_count)


string1=input("enter a string:")
no_of_upperandlower(string1)

