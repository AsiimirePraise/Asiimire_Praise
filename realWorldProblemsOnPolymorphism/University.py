# Demonstrating method overriding, method overloading, and MRO
from multipledispatch import dispatch
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

    def write_exam(self):
        print(f"{self.name} is not allowed to write exams unless they are a student.")

    def pay_tuition(self):
        print(f"{self.name} cannot pay tuition as they are not a student.")


class Lecturer(Person):
    def __init__(self, name, age, gender, lecturer_id):
        super().__init__(name, age, gender)
        self.lecturer_id = lecturer_id

    def display(self):
        print(f"LECTURER \nName: {self.name}, Age: {self.age}, Gender: {self.gender}, ID: {self.lecturer_id}")

    def teach_course(self, course):
        print(f"Lecturer {self.name} is teaching {course}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, hall_of_attachment):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.hall_of_attachment = hall_of_attachment

    def display(self):
        print(f"STUDENT \nName: {self.name}, Age: {self.age}, Gender: {self.gender}, ID: {self.student_id}, Hall: {self.hall_of_attachment}")

    @dispatch(str)
    def write_exam(self,name):
        print(f"Student {self.name} is writing a general exam.")

    @dispatch(str,str)
    def write_exam(self, subject,name):
        print(f"Student {self.name} is writing the {subject} exam.")
        
    @dispatch(int)
    def pay_tuition(self,amount):
        print(f"Student {self.name} is paying tuition fees of ${amount}.")
        print("Payment successful!")

class Parent(Person):
    def __init__(self, name, age, gender, student_name, contact):
        super().__init__(name, age, gender)
        self.student_name = student_name
        self.contact = contact

    def display(self):
        print(f"PARENT \nName: {self.name}, Age: {self.age}, Gender: {self.gender}, Student: {self.student_name}, Contact: {self.contact}")

    @dispatch(int)
    def pay_student_fees(self,amount):
        print(f"Parent {self.name} is paying ${amount} for student {self.student_name}")
        print("Payment successful!")

    @dispatch(int,str)
    def pay_student_fees(self, amount,name):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        print(f"Parent {self.name} is paying ${amount} for student {self.student_name}")
        print("Payment successful!")
print("---------------------------------------------------------------")
student1 = Student("Praise", 22, "Female", "U345", "Africa Hall")
student1.display()
student1.write_exam("Mathematics","praise")  
student1.pay_tuition(7999)
print("---------------------------------------------------------------")
parent = Parent("Mr. Samson", 50, "Male", "Praise", "127")
parent.display()
parent.pay_student_fees(7777,"praise")
print("---------------------------------------------------------------")
lecturer = Lecturer("Dr. Johnson", 40, "Male", "L789")
lecturer.display()
lecturer.teach_course("Computer Science")
lecturer.write_exam()
