class Hospital:
    def __init__(self,admin,doctor,sister,department):
        self.admin = admin
        self.doctor =doctor
        self.sister = sister
        self.department = department

    def givedetail(self):
        self.admin = input("Enter the Name of Admin")  
        self.doctor = input("Enter the Name of Doctor") 
        self.sister = input("Enter the Name of Sister") 
        self.department = input("Enter the Name of Department") 
        
class Department(Hospital):
    def printdetails(self):
        print(self.admin,self.department,self.doctor,self.sister)

class PatientWard:
    def __init__(self,pname,disease,age):
        self.pname = pname
        self.disease =disease
        self.age = age

    
    def Pgivedetail(self):
        self.pname = input("Enter the Name of Patient")  
        self.disease = input("Enter the Disease") 
        self.age = input("Enter the Age") 
       
    def Pprintdetails(self):
        print("Patient Name" + self.pname,self.disease,self.age)  
        print("Patient Disease" + self.disease,self.age)  
        print("Patient Age" + self.age)    


hosp = Department("","","","")
hosp.givedetail()
hosp.printdetails()

 




































