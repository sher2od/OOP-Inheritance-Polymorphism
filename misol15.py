class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defend(self):
        pass

class Warrior(Character):
    def attack(self):
        return f"{self.name} qilich bilan hujum qildi!"

    def defend(self):
        return f"{self.name} qalqon bilan himoyalandi."

class Mage(Character):
    def attack(self):
        return f"{self.name} sehrli o'q otmoqda!"

    def defend(self):
        return f"{self.name} sehrli to‘siq qo‘ydi."

class Archer(Character):
    def attack(self):
        return f"{self.name} kamon bilan otmoqda!"

    def defend(self):
        return f"{self.name} tezlik bilan chetga o‘tdi."

# Misollar
w = Warrior("Bahodir")
m = Mage("Zuhra")
a = Archer("Temur")

print(w.attack())   # Bahodir qilich bilan hujum qildi!
print(m.attack())   # Zuhra sehrli o'q otmoqda!
print(a.attack())   # Temur kamon bilan otmoqda!

print(w.defend())   # Bahodir qalqon bilan himoyalandi.
print(m.defend())   # Zuhra sehrli to‘siq qo‘ydi.
print(a.defend())   # Temur tezlik bilan chetga o‘tdi.
