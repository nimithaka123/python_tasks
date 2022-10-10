input_list=[]
odd_item_list=[]
length=int(input("enter length of the string:"))
for i in range(length):
    item=input("enter the items of the list:")
    input_list.append(item)
for i in range(length):
    if i%2!=0:
        odd_item_list.append(input_list[i])
print("the entered list is:", input_list)
print("the odd index elements from the entered list is:")
print(odd_item_list)