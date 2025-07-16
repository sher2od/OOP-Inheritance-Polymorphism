class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Admin(User):
    def  access_level(self):
        return f"{self.name},Full access granted" 

class Guest(User):
    def access_level(self):
        return f"{self.name} Limited access only"
    

a = Admin('vali',19)
print(a.access_level())

g = Guest('ali',22)
print(g.access_level())



































