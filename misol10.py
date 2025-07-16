class Document:
    def __init__(self, title):
        self.title = title

class WordDocument(Document):
    def print_preview(self):
        return f"{self.title} hujjati Word formatida ko‘rsatilmoqda..."

class PdfDocument(Document):
    def print_preview(self):
        return f"{self.title} hujjati PDF formatida ko‘rsatilmoqda..."

doc1 = WordDocument("Shartnoma")
print(doc1.print_preview())

doc2 = PdfDocument("Hisobot")
print(doc2.print_preview())
