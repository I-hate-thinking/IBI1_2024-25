class Patient:  
    def __init__(self, name, age, admission_date, medical_history): # input the information of the patients
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history
    
    def print_details(self): # print out all the detailed information of the patient
        print(f"patients: {self.name}, age: {self.age}, the date of recent hospitalization: {self.admission_date}, medical history: {self.medical_history}")


# example
if __name__ == "__main__":
    # create two example
    patient1 = Patient("Tom", 35, "2023-05-15", "diabetes")
    patient2 = Patient("Amy", 28, "2023-06-20", "asthma")
    
    # print the information 
    print("hospital patient records:")
    patient1.print_details()
    patient2.print_details()