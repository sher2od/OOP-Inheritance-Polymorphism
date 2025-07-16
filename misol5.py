from abc import ABC, abstractmethod

# Abstract klass
class Appliance(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# TV klassi
class Tv(Appliance):
    def turn_on(self):
        return f"{self.name} yoqildi (TV)"

    def turn_off(self):
        return f"{self.name} o'chirildi (TV)"

# Muzlatkich klassi
class Fridge(Appliance):
    def turn_on(self):
        return f"{self.name} ishga tushdi (Fridge)"

    def turn_off(self):
        return f"{self.name} o'chdi (Fridge)"

# Test qilish
devices = [
    Tv("Samsung TV"),
    Fridge("LG Muzlatkich")
]

for device in devices:
    print(device.turn_on())
    print(device.turn_off())
