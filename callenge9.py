class Computer:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def getspecs(self):
        self.name =input("Enter the System Name ")      
        self.price =input("Enter the Price ")

    def displayspecs(self):
        print(self.name,self.price)



class Desktop(Computer):
    def __init__(self,ram,processor,HDD):
        self.ram=ram
        self.processor=processor
        self.HDD = HDD

    def getspecz(self):
        self.name =input("Enter the Size of Ram ")      
        self.HDD =input("Enter the Size of Harddisk ")
        self.processor =input("Enter the Processor ")

    def displayspecz(self):
        print(self.ram,self.HDD,self.processor)

class Laptop(Computer):
    def __init__(self,ram,processor,SSD):
        self.ram=ram
        self.processor=processor
        self.SSD = SSD

    def getspec(self):
        self.name =input("Enter the Size of Ram ")      
        self.SSD =input("Enter the Size of SSD ")
        self.processor =input("Enter the Processor ")

    def displayspec(self):
        print(self.ram,self.SSD,self.processor)

dsk = Desktop("","","")
dsk.getspecs()
dsk.displayspecs()
dsk.getspecz()
dsk.displayspecz()