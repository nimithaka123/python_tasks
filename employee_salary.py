emp_id=int(input("enter employee id:"))
emp_name=input("enter employee name:")
basic_pay=int(input("enter basic pay:"))
if basic_pay>10000:
    hra=(15*basic_pay)/100
    da=(8*basic_pay)/100
    # net_pay=basic_pay+hra+da
if basic_pay>5000 and basic_pay<=10000:
    hra=(10*basic_pay)/100
    da=(5*basic_pay)/100
    # net_pay=basic_pay+hra+da  
if basic_pay==5000:
    hra=(5*basic_pay)/100
    da=(3*basic_pay)/100
net_pay=basic_pay+hra+da  
print("id:",emp_id)
print("name:",emp_name)
print("salary details are:")
print("basic pay:",basic_pay)
print("DA:",da)
print("HRA:",hra)
print("net pay:", net_pay)



