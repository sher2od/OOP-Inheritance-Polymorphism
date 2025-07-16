class Courier:
    def __init__(self, product, distance):
        self.product = product
        self.distance = distance

class BikeCourier(Courier):
    def delivery_range(self):
        return f"{self.product}, {self.distance} km gacha velosiped bilan yetkaziladi"
    
    def calculate_fee(self):
        return self.distance * 1000 

class CarCourier(Courier):
    def delivery_range(self):
        return f"{self.product}, {self.distance} km gacha mashina bilan yetkaziladi"
    
    def calculate_fee(self):
        return self.distance * 2000 + 5000  
    
class DroneCourier(Courier):
    def delivery_range(self):
        return f"{self.product}, {self.distance} km gacha dron orqali yetkaziladi"
    
    def calculate_fee(self):
        return self.distance * 3000 


b = BikeCourier("Kitob", 3)
c = CarCourier("Televizor", 20)
d = DroneCourier("Hujjat", 7)

print(b.delivery_range(), "| Narx:", b.calculate_fee())
print(c.delivery_range(), "| Narx:", c.calculate_fee())
print(d.delivery_range(), "| Narx:", d.calculate_fee())
