class User:
    def __init__(self,name,course):
        self.name = name
        self.course = course

class Student(User):
    def get_dashboard(self):
        return f" {self.name},{self.course} Kurslarga qatnashmoqda"
    
class Instructor(User):
    def get_dashboard(self):
        return f"{self.name},{self.course} Kurslarni yaratgan"
    

users = [
    Student("Dilshod","Dasturlash ,Ing tili"),
    Instructor("Begzod","Kimyo,Matematika")
    
]

for user in users:
    print(user.get_dashboard())