string1=input("enter a string:")
vowels=set('aeiouAEIOU')
count=0
for i in string1:
    if i in vowels:
        count=count+1
print("the no of vowels in the given string is:", count)
