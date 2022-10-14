class student:

    def __init__(self):

        self.rollno=0
        self.name=" "
    

    def get_data(self):
        self.rollno=int(input("enter the roll no:"))
        self.name=input("enter the name:")



    def print_data(self):
        print("Roll:", self.rollno)
        print("Name:",self.name)


class marks(student):
    
    def __init__(self):
        self.english=0
        self.maths=0
        self.science=0
        self.history=0
        self.sociology=0
        self.computer=0

    def input_data(self):
        self.get_data()
        self.english=int(input("enter the mark of english:"))
        self.maths=int(input("enter the mark of Maths:"))
        self.science=int(input("enter the mark of Science:"))
        self.history=int(input("enter the mark of history:"))
        self.sociology=int(input("enter the mark of sociology:"))
        self.computer=int(input("enter the mark of computer:"))

    def out_data(self):
        self.print_data()
        print("Mark of Subjects:")
        print("English:",self.english)
        print("Maths:",self.maths)
        print("Science:",self.science)
        print("History:",self.history)
        print("Sociology:",self.sociology)
        print("Computer:",self.computer)

    

# student1=student()
# student1.get_data()
# student1.print_data()

student1=marks()
student1.input_data()
student1.out_data()
