sum_odd=sum_even=0
for i in range(15,36):
    if i%2==0:
        sum_even=sum_even+i
    else:
        sum_odd=sum_odd+i
print("sum of even numbers from 15 to 35 are:",sum_even)
print("sum of odd numbers from 15 to 35 are:",sum_odd)

