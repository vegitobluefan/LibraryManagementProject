class Book:
    """Класс отдельной книги, содержит поля: title, author, year, status."""

    def __init__(self, book_id: int, title: str,
                 author: str, year: int, status: str):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return (
            f"id: {self.id}, Название: {self.title}, Автор: {self.author}, "
            f"Год издания: {self.year}, Статус: {self.status}")


class Library:
    """Класс библиотеки, содержащий методы для взаимодействия с книгами."""

    def __init__(self):
        self.books = []

    def get_book_by_id(self, book_id: int):
        """Получение книги по id."""
        return next((book for book in self.books if book.id == book_id), None)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавление книги в библиотеку."""
        if not title or not author:
            print("Ошибка: поля заполнены некорректно.")
            return

        for book in self.books:
            if (
                book.title == title and book.author == author
                and book.year == year
            ):
                print(f"Книга '{title}' уже существует в библиотеке.")
                return

        book_id = max([book.id for book in self.books], default=0) + 1
        status = "в наличии"
        new_book = Book(book_id, title, author, year, status)
        self.books.append(new_book)
        print(f"Книга '{title}' добавлена в библиотеку.")

    def remove_book(self, book_id: int) -> None:
        """Удаление книги по id."""
        book = self.get_book_by_id(book_id)
        if book:
            self.books.remove(book)
            print("Книга успешно удалена из библиотеки.")
        else:
            print("Книга не найдена.")

    def find_books(self, query: str) -> list[Book]:
        """Поиск книги по title, author или year."""
        found_books = [
            book for book in self.books if query.lower() in book.title.lower()
            or query.lower() in book.author.lower()
            or query == str(book.year)
        ]
        return found_books

    def display_books(self) -> None:
        """Отображение всех книг в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
        else:
            print("Все книги в библиотеке:")
            for book in self.books:
                print(book)

    def update_book_status(self, book_id: int, new_status: str) -> None:
        """Обновление статуса книги."""
        valid_statuses = ("в наличии", "выдана")
        if new_status not in valid_statuses:
            print("Ошибка: некорректный статус.")
            return

        book = self.get_book_by_id(book_id)
        if book:
            book.status = new_status
            print(f'Статус книги изменен на "{new_status}".')
        else:
            print("Книга не найдена.")


def print_menu():
    print("\nМеню:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу по названию, автору, году")
    print("4. Показать все книги")
    print("5. Изменить статус книги")
    print("6. Выход")


def main():
    library = Library()

    while True:
        print_menu()
        action = input("Выберите действие: ")

        if action == "1":
            try:
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания: "))
                library.add_book(title, author, year)
            except ValueError:
                print("Ошибка: год должен быть числом.")

        elif action == "2":
            try:
                book_id = int(input("Введите id книги для удаления: "))
                library.remove_book(book_id)
            except ValueError:
                print("Ошибка: id должен быть числом.")

        elif action == "3":
            query = input("Введите название, автора или год: ")
            results = library.find_books(query)
            if results:
                for book in results:
                    print(book)
            else:
                print("Книга не найдена.")

        elif action == "4":
            library.display_books()

        elif action == "5":
            try:
                book_id = int(input("Введите id книги: "))
                new_status = input("Введите новый статус (в наличии/выдана): ")
                library.update_book_status(book_id, new_status)
            except ValueError:
                print("Ошибка: id должен быть числом.")

        elif action == "6":
            print("Выход из программы.")
            break
        else:
            print("Ошибка, выберите один из доступных вариантов.")


if __name__ == "__main__":
    main()
