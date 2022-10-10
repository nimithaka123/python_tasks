rollno=[44,64,69,37,76,83,95,97]
sample_dict={'sojo':44,'thomas':69,'tom':76,'jack':11}
for i in rollno[:]:
    if i not in sample_dict.values():
            rollno.remove(i)
print("the elements both in list and dictionary values are: ")
print(rollno)


