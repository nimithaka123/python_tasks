class employee:
    def __init__(self):
        self.employee_id=0
        self.employee_name=" "
        self.employee_desig=" "
        self.employee_address=" "
        self.employee_phone=" "

    def get_data(self):
        self.employee_id=int(input("enter the employee id:"))
        self.employee_name=input("enter the employee name:")
        self.employee_desig=input("enter the employee designation:")
        self.employee_address=input("enter the employee address:")
        self.employee_phone=input("enter the employee phone no:")

    def put_data(self):
        # self.get_data()
        print("****************")
        print("Employee id:",self.employee_id)
        print("Employee name:",self.employee_name)
        print("Employee designation:",self.employee_desig)
        print("Employee address:",self.employee_address)
        print("Employee phone no:",self.employee_phone)

class salary(employee):

    def __init__(self):
        self.basic_pay=0
        self.da=0
        self.hra=0
        self.pf=0
        self.net_pay=0

    def input_data(self):
        self.get_data()
        self.basic_pay=int(input("enter the basic pay:"))

    def calculate(self):
        if self.basic_pay>=10000:
            self.hra=round((15*self.basic_pay)/100,2)
            self.da=round((8*self.basic_pay)/100,2)
            self.pf=round((10*self.basic_pay)/100,2)
        if self.basic_pay>5000 and self.basic_pay<10000:
            self.hra=round((10*self.basic_pay)/100,2)
            self.da=round((5*self.basic_pay)/100,2)
            self.pf=round((8*self.basic_pay)/100,2)
        else:
            self.hra=round((5*self.basic_pay)/100,2)
            self.da=round((3*self.basic_pay)/100,2)
            self.pa=round((1*self.basic_pay)/100,2)
        self.net_pay=self.basic_pay+self.hra+self.da+self.pf

    def display(self):
        self.put_data()
        print("Salary details are:")
        print("Basic pay is:",self.basic_pay)
        print("HRA is:",self.hra)
        print("DA is:",self.da)
        print("PF is:",self.pf)
        print("Net pay is:",self.net_pay)







# employee1=employee()
# employee1.get_data()
# employee1.put_data()

employee1=salary()
employee1.input_data()
employee1.calculate()
employee1.display()


