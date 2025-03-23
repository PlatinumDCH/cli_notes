import os
import pickle
from typing import Optional, Any


def read_data_from_file(filename: str) -> Optional[Any]:
    """
    Читает данные их файла и испольpзованием picle
    
    :param filename: Имя фала для чтения
    :return: Десерелихованные данные или None, если файл пустой или не существует.
    """
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return


def write_data_to_file(filename: str, book: Any) -> None:
    """
    Записывает данные в файл с использованием pickle.

    :param filename: Имя файла для записи.
    :param book: Данные, которые нужно сохранить.
    """
    with open(filename, 'wb') as file:
        pickle.dump(book, file)
