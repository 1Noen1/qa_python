conftest.py - вспомогательная функция (фикстура)
main.py - класс BooksCollector
tests.py - тестовый класс TestBooksCollector

Набор тестовых методов класса TestBooksCollector:

Позитивные тесты:
test_add_new_book_add_two_books: Проверка добавления двух книг в словарь books_genre
test_add_new_book_adding_three_books_success: Проверка добавления трёх книг в словарь books_genre
test_set_book_genre_added: Проверка добавления жанра книге из списка genre
test_set_book_genre_changed: Проверка изменения жанра книги из списка genre
test_get_book_genre_returns_correct_genre: Проверка корректного возврата жанра книги методом get_book_genre (без использования set_book_genre)
test_get_book_genre_returns_empty_if_no_genre: Проверка возврата пустого жанра для книги без жанра
test_get_books_genre_positive: Проверка корректного возврата словаря books_genre методом get_books_genre
test_get_books_with_specific_genre_success: Проверка вывода книги определённого жанра
test_get_books_for_children_success: Проверка вывода списка книг с жанром для детей
test_add_book_in_favorites_add_one_book_added: Проверка добавления книги из списка books_genre в избранное
test_get_list_of_favorites_books_positive: Отдельная проверка метода get_list_of_favorites_books
test_delete_book_from_favorites_book_deleted: Проверка удаления книги из списка избранного

Негативные тесты:
test_add_new_book_add_incorrect_name_not_added: Негативная проверка добавления книг с пустым именем или больше 40 символов (параметризированный тест)
test_add_new_book_add_double_books_not_added: Негативная проверка повторного добавления одинаковых книг
test_set_book_genre_missing_genre_not_added: Негативная проверка добавления жанра не из списка genre
test_get_books_with_specific_genre_missing_book: Негативная проверка вывода отсутствующей книги определённого жанра
test_add_book_in_favorites_add_missing_book_not_added: Негативная проверка добавления книги не из списка books_genre в избранное
test_add_book_in_favorites_add_double_books_not_added: Негативная проверка повторного добавления книги в избранное
test_delete_book_from_favorites_missing_book_not_deleted: Негативная проверка удаления книги не из списка избранного

Команда для запуска тестов:
pytest -v

Результат выполнения 20 тестов: 100%