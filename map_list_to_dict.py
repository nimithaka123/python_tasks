# name=['ammu','raju','appu']
# mark=[10,20,30]
name=[]
mark=[]
dict1={}
length=int(input("enter the length of list:"))
print("first list:")
for i in range(length):
    item=input("enter elements of list1:")
    name.append(item)
print("second list:")
for i in range(length):
    item=int(input("enter elements of list2:"))
    mark.append(item)
for i in range(length):
        dict1[name[i]]=mark[i]
print("the dictionary is:")
print(dict1)
