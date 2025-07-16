class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            return "Yetarli mablag' yo'q"
        self.balance -= amount
        return f"Omonat hisobidan {amount} so'm yechildi. Qolgan: {self.balance}"

    def get_interest(self):
        interest = self.balance * 0.05  # 5% foyda
        return f"Omonat hisobidagi foiz: {interest} so'm"

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount  # overdaft ruxsat — minusga kiradi
        return f"Hisobdan {amount} so'm yechildi. Hozirgi balans: {self.balance}"

    def get_interest(self):
        return "Bu hisobga foiz qo‘llanilmaydi"

acc1 = SavingsAccount(1_000_000)
print(acc1.withdraw(200_000))
print(acc1.get_interest())

acc2 = CheckingAccount(500_000)
print(acc2.withdraw(600_000))  # Overdraft holat
print(acc2.get_interest())
