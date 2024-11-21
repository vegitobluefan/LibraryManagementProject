import unittest
from library import Book, Library


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book(1, "Обломов", "И. Гончаров", 1859, "в наличии")
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Обломов")
        self.assertEqual(book.author, "И. Гончаров")
        self.assertEqual(book.year, 1859)
        self.assertEqual(book.status, "в наличии")
        self.assertIsInstance(str(book), str)


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Обломов", "И. Гончаров", 1859)
        self.assertEqual(len(self.library.books), 1)
        book = self.library.books[0]
        self.assertEqual(book.title, "Обломов")
        self.assertEqual(book.author, "И. Гончаров")
        self.assertEqual(book.year, 1859)
        self.assertEqual(book.status, "в наличии")

    def test_remove_book(self):
        self.library.add_book("Обломов", "И. Гончаров", 1859)
        book_id = self.library.books[0].id
        self.library.remove_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_find_books(self):
        self.library.add_book("Обломов", "И. Гончаров", 1859)
        self.library.add_book("Обрыв", "И. Гончаров", 1869)
        results = self.library.find_books("Обломов")
        self.assertEqual(len(results), 1)  # 1 книга Обломов
        results = self.library.find_books("И. Гончаров")
        self.assertEqual(len(results), 2)  # 2 книги Гончарова
        results = self.library.find_books("2019")
        self.assertEqual(len(results), 0)  # Нет книг за 2019 год

    def test_update_book_status(self):
        self.library.add_book("Обломов", "И. Гончаров", 1859)
        book_id = self.library.books[0].id
        self.library.update_book_status(book_id, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")  # Статус обновлен
        self.library.update_book_status(book_id, "в наличии")
        self.assertEqual(self.library.books[0].status, "в наличии")  # Статус восстановлен
        self.library.update_book_status(book_id, "неизвестный статус")  # Некорректный статус
        self.assertEqual(self.library.books[0].status, "в наличии")  # Статус не изменился
