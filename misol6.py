class Employee:
    def __init__(self,selary):
        self.selary = selary

        

class Developer(Employee):
    def calculate_bonus(self):
        return self.selary * 0.10

class Meneger(Employee):
    def calculate_bonus(self):
        return self.selary * 0.20
    
ob1 = Developer(5_000_000)
print(ob1.calculate_bonus()) 

bo2 = Meneger(9_000_000)
print(bo2.calculate_bonus())