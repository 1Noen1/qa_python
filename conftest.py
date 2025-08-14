import pytest
from main import BooksCollector


@pytest.fixture
def collection():
    """Создаёт пустой экземпляр коллектора книг"""
    return BooksCollector()


def pytest_make_parametrize_id(val):
    """Для корректного отображения аргументов в параметризированном тесте"""
    return repr(val)
