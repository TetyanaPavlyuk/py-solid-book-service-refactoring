import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayBook(ABC):
    @abstractmethod
    def display_book(self, book: Book) -> None:
        pass


class DisplayBookConsole(DisplayBook):
    def display_book(self, book: Book) -> None:
        print(book.content)


class DisplayBookReverse(DisplayBook):
    def display_book(self, book: Book) -> None:
        print(book.content[::-1])


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintBookConsole(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintBookReverse(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializeBookJSON(SerializeBook):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeBookXML(SerializeBook):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                DisplayBookConsole().display_book(book)
            if method_type == "reverse":
                DisplayBookReverse().display_book(book)
        elif cmd == "print":
            if method_type == "console":
                PrintBookConsole().print_book(book)
            if method_type == "reverse":
                PrintBookReverse().print_book(book)
        elif cmd == "serialize":
            if method_type == "json":
                return SerializeBookJSON().serialize(book)
            if method_type == "xml":
                return SerializeBookXML().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
