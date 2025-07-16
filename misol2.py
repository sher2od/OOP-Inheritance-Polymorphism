class Vehicle:
    def __init__(self,nomi,modeli):
        self.nomi = nomi
        self.modeli = modeli

class Car(Vehicle):
    def show_info(self):
        return f"{self.nomi},{self.modeli}"
    
class Bike(Vehicle):
    def show_info(self):
        return f"{self.nomi},{self.modeli}"
    
c = Car('Tesla','S 2020')
print(c.show_info())

b = Bike('Yamaha','Sport 2020')
print(b.show_info())