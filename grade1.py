eng=int(input("enter mark of english:"))
mal=int(input("enter mark of malayalam:"))
phy=int(input("enter mark of physics:"))
mat=int(input("enter mark of mathematics:"))
chem=int(input("enter mark of chemistry:"))
cs=int(input("enter mark of computer science:"))
total=eng+mal+phy+mat+chem+cs
print("total mark is:", total)
avg_m=total/6
print(round(avg_m,2))
if avg_m>=90:
    print("Grade is: A+")
elif avg_m>=80 and avg_m<90:
    print("Grade is: A")
elif avg_m>=70 and avg_m<80:
    print("Grade is: B+")
elif avg_m>=60 and avg_m<70:
    print("Grade is: B")
elif avg_m>=50 and avg_m<60:
    print("Grade is: C+")
elif avg_m>=40 and avg_m<50:
    print("Grade is: C")
else:
    print("Grade is: D")