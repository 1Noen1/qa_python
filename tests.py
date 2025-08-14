import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collection = BooksCollector()
        collection.add_new_book('Гордость и предубеждение и зомби')
        collection.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collection.get_books_genre()) == 2

    def test_add_new_book_adding_three_books_success(self):
        collection = BooksCollector()
        books = ['Ромео и Джульетта', 'Мастер и Маргарита', 'Король Лев']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 3

    def test_add_new_book_check_genre_success(self):
        collection = BooksCollector()
        first_book = 'Ромео и Джульетта'
        collection.add_new_book(first_book)
        assert collection.get_book_genre(first_book) == ''

    def test_get_book_genre_returns_correct_genre(self):
        collection = BooksCollector()
        book = 'Книга1'
        collection.add_new_book(book)
        collection.set_book_genre(book, 'Фантастика')
        assert collection.get_book_genre(book) == 'Фантастика'

    @pytest.mark.parametrize('book', ['', 'МастерМастерМастерМастерМастерМастерМастер'])
    def test_add_new_book_add_incorrect_name_not_added(self, book):
        collection = BooksCollector()
        collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 0

    def test_add_new_book_add_double_books_not_added(self):
        collection = BooksCollector()
        books = ['Война и мир', 'Война и мир']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 1

    def test_set_book_genre_changed(self):
        collection = BooksCollector()
        first_book = 'Властелин колец'
        genre = 'Фантастика'
        other_genre = 'Детективы'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        collection.set_book_genre(first_book, other_genre)
        assert collection.get_book_genre(first_book) == other_genre

    def test_set_book_genre_added(self):
        collection = BooksCollector()
        first_book = 'Властелин колец'
        genre = 'Фантастика'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        assert collection.get_book_genre(first_book) == genre

    def test_set_book_genre_missing_genre_not_added(self):
        collection = BooksCollector()
        first_book = 'Властелин колец'
        missing_genre = 'Приключения'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, missing_genre)
        assert collection.get_book_genre(first_book) == ''

    def test_get_books_with_specific_genre_success(self):
        collection = BooksCollector()
        books = ['Властелин колец', 'Король лев', 'Чужой', 'Сон в летнюю ночь', 'Молчание ягнят']
        genres = ['Фантастика', 'Мультфильмы', 'Ужасы', 'Комедии', 'Детективы']
        for i in range(5):
            collection.add_new_book(books[i])
            collection.set_book_genre(books[i], genres[i])
        assert collection.get_books_with_specific_genre('Ужасы') == ['Чужой']

    def test_get_books_with_specific_genre_missing_book(self):
        collection = BooksCollector()
        books = ['Властелин колец', 'Король лев']
        genres = ['Фантастика', 'Мультфильмы']
        for i in range(2):
            collection.add_new_book(books[i])
            collection.set_book_genre(books[i], genres[i])
        assert len(collection.get_books_with_specific_genre('Приключения')) == 0

    def test_get_books_for_children_success(self):
        collection = BooksCollector()
        books = ['Властелин колец', 'Король лев', 'Чужой', 'Сон в летнюю ночь', 'Молчание ягнят']
        genres = ['Фантастика', 'Мультфильмы', 'Ужасы', 'Комедии', 'Детективы']
        for i in range(5):
            collection.add_new_book(books[i])
            collection.set_book_genre(books[i], genres[i])
        children_books = collection.get_books_for_children()
        assert len(children_books) == 3 and children_books == ['Властелин колец', 'Король лев', 'Сон в летнюю ночь']

    def test_add_book_in_favorites_add_one_book_added(self):
        collection = BooksCollector()
        first_book = 'Хоббит'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        assert collection.favorites == [first_book]

    def test_add_book_in_favorites_add_missing_book_not_added(self):
        collection = BooksCollector()
        first_book = 'Властелин колец'
        collection.add_book_in_favorites(first_book)
        assert collection.favorites == []

    def test_add_book_in_favorites_add_double_books_not_added(self):
        collection = BooksCollector()
        first_book = 'Властелин колец'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.add_book_in_favorites(first_book)
        assert collection.favorites == [first_book]

    def test_delete_book_from_favorites_book_deleted(self):
        collection = BooksCollector()
        first_book = 'Властелин колец'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(first_book)
        assert collection.favorites == []

    def test_delete_book_from_favorites_missing_book_not_deleted(self):
        collection = BooksCollector()
        first_book = 'Хоббит'
        second_book = 'Властелин колец'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(second_book)
        assert collection.favorites == [first_book]
