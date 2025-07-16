class User:
    def __init__(self, name):
        self.name = name

class Applicant(User):
    def interact(self):
        return self.apply_to_job()

    def apply_to_job(self):
        return f"{self.name} ishga ariza topshirdi."

class Employer(User):
    def interact(self):
        return self.post_job()

    def post_job(self):
        return f"{self.name} yangi ish joyi e'lon qildi."

# Misollar
a = Applicant("Ali")
e = Employer("TechCorp")

print(a.interact())  
print(e.interact()) 