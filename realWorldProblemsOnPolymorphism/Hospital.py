from multipledispatch import dispatch

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
    
    @dispatch()
    def schedule_appointment(self):
        print(f"{self.name} scheduled a general appointment.")

class Patient(Person):
    def __init__(self, name, age, gender, patientID):
        super().__init__(name, age, gender)
        self.patientID = patientID

    def display_info(self):
        print(f"PATIENT \nName: {self.name}, Age: {self.age}, Gender: {self.gender}, ID: {self.patientID}")
    
    @dispatch(str, str)
    def schedule_appointment(self, date, time):
        print(f"{self.name} scheduled an appointment on {date} at {time}.")

    def enter_appointment(self):
        date = input("Enter the appointment date: ")
        time = input("Enter the appointment time: ")
        self.schedule_appointment(date, time)

class Doctor(Person):
    def __init__(self, name, age, gender, doctorID):
        super().__init__(name, age, gender)
        self.doctorID = doctorID

    def display_info(self):
        print(f"DOCTOR \nName: {self.name}, ID: {self.doctorID}, Age: {self.age}, Gender: {self.gender}")

    def view_patient(self, patient):
        print(f"Doctor {self.name} is viewing patient info:")
        patient.display_info()

    def verify_doctor(self, patient):
        choice = input("Are you a doctor? (yes/no): ").lower()
        if choice == "yes":
            self.view_patient(patient)
        else:
            print("Access denied: Only doctors can view patient info.")

patient1=Patient("praise",78,"female","p099")
patient1.display_info()
patient1.enter_appointment()
print("------------------------------------------------")

doctor1=Doctor("Dr.Praise",6,"male","D01")
doctor1.verify_doctor(patient1)
doctor1.display_info()