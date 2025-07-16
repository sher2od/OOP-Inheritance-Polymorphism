# Ota klass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} doesn't know how to speak"

# Farzand klass - Dog
class Dog(Animal):
    def speak(self):
        return f"{self.name} vov vov"

# Farzand klass - Cat
class Cat(Animal):
    def speak(self):
        return f"{self.name} meow meow"

# Test qilish
a = Animal("Hayvon")
print(a.speak())   # Hayvon doesn't know how to speak

d = Dog("it")
print(d.speak())   # it vov vov

c = Cat("mushuk")
print(c.speak())   # mushuk meow meow












