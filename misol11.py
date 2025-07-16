class Product:
    def __init__(self,product):
        self.product = product

class PhysicalProduct(Product):
    def get_delivery_method(self):
        return f"{self.product} Pochta orqali jonatildi"
    
class DigitalProduct(Product):
    def get_delivery_method(self):
        return f"{self.product} internet orqali uzatildi"

mahsulotlar = [
    PhysicalProduct("Phone"),
    DigitalProduct("Pdf")
]
        
for mahsulot in mahsulotlar:
    print(mahsulot.get_delivery_method())
