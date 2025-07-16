class Media:
    def __init__(self,m_name):
        self.m_name = m_name

class Song(Media):
    def play(self):
        return f"{self.m_name} Qoshiq ijro etadi "
    
class Movie(Media):
    def play(self):
        return f"{self.m_name} filim ishga tushdi "
    
class Podcast(Media):
    def play(self):
        return f"{self.m_name} Podcast tinglanmoqda"
    
devices = [
    Song("Ali"),
    Movie("Tubanlik"),
    Podcast("Anvar Narzullayev")
]

for device in devices:
    print(device.play())