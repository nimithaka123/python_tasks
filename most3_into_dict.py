input_list=[]
count_dict1={}
length=int(input("enter the length of the list:"))
for i in range(length):
    item=input("enter the elements of the list:")
    input_list.append(item)
print("the entered list is:")
print(input_list)
for i in input_list:
    if i not in count_dict1:
        count_dict1[i]=input_list.count(i)
sorted_dict=sorted(count_dict1.items(), key = lambda kv: kv[1])
sorted_list=list(sorted_dict)
sorted_list.reverse()    
most_occur_list=sorted_list[0:3]
most_occur_dict = dict(most_occur_list)
print("words and count in the dictionary form is:")
print(count_dict1)
print("most three occured word and it's count is:")
print(most_occur_dict)
