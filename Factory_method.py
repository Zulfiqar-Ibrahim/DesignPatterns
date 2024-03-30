from abc import ABC, abstractmethod
class Document(ABC):
    @abstractmethod
    def show(self):
        pass

class PDFDocument(Document):
    def show(self):
        print("PDF Document")

class WordDocument(Document):
    def show(self):
        print("Word Document")
class DocumentCreator(ABC):
    def create_document(self) -> Document:
        pass
class PDFDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PDFDocument()
class WordDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()
if __name__ == "__main__":
    pdf_creator = PDFDocumentCreator()
    pdf_document = pdf_creator.create_document()
    pdf_document.show()

    word_creator = WordDocumentCreator()
    word_document = word_creator.create_document()
    word_document.show()