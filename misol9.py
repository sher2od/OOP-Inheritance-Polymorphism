class Notification:
    def __init__(self,massage):
        self.massage = massage

class EmailNotification(Notification):
    def send(self):
        return f"{self.massage} xabar Email orqali uzatildi"

class SMSNotification(Notification):
    def send(self):
        return f"{self.massage} xabar sms orqali ketti"
    
ob1 = EmailNotification("Assalom")
print(ob1.send())

ob2 = SMSNotification("Assalom")
print(ob2.send())