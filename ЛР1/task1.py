import doctest
from typing import Union, List, Optional


class Book:
    """
    Класс для представления книги в библиотеке.
    """

    def __init__(self, title: str, author: str, year: int, pages: int):
        """
        Создание объекта "Книга".

        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 672)
        >>> book.title
        'Преступление и наказание'
        >>> book.author
        'Фёдор Достоевский'
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if len(title.strip()) == 0:
            raise ValueError("Название книги не может быть пустым")
        self.title: str = title

        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if len(author.strip()) == 0:
            raise ValueError("Автор не может быть пустым")
        self.author: str = author

        if not isinstance(year, int):
            raise TypeError("Год издания должен быть целым числом")
        if year < 0 or year > 2026:
            raise ValueError("Год издания должен быть от 0 до 2026")
        self.year: int = year

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages: int = pages

    def is_classic_literature(self, current_year: Optional[int] = None) -> bool:
        """
        Проверяет, является ли книга классической литературой.

        :param current_year: Текущий год
        :return: True если книга издана более 100 лет назад, False если нет

        Примеры:
        >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 672)
        >>> book.is_classic_literature()
        True
        """
        ...

    def estimate_reading_time(self, pages_per_day: Union[int, float] = 50) -> float:
        """
        Оценивает количество дней для прочтения книги.

        :param pages_per_day: Количество страниц, читаемых в день
        :return: Количество дней для прочтения

        Примеры:
        >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 672)
        >>> book.estimate_reading_time(30)
        22.4
        """
        ...

    def get_book_info(self) -> str:
        """
        Возвращает информацию о книге.

        :return: Строка с информацией о книге

        Примеры:
        >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 672)
        >>> book.get_book_info()
        'Преступление и наказание, Фёдор Достоевский, 1866 год, 672 страницы'
        """
        ...


class Car:
    """
    Класс для представления автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int, engine_volume: float):
        """
        Создание объекта "Автомобиль".

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска
        :param engine_volume: Объем двигателя в литрах

        Примеры:
        >>> car = Car("Toyota", "Land Cruiser 200", 2018, 4.6)
        >>> car.brand
        'Toyota'
        >>> car.model
        'Land Cruiser 200'
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if len(brand.strip()) == 0:
            raise ValueError("Марка автомобиля не может быть пустой")
        self.brand: str = brand

        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if len(model.strip()) == 0:
            raise ValueError("Модель автомобиля не может быть пустой")
        self.model: str = model

        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом")
        if year < 1886 or year > 2026:
            raise ValueError("Год выпуска должен быть от 1886 до 2026")
        self.year: int = year

        if not isinstance(engine_volume, (int, float)):
            raise TypeError("Объем двигателя должен быть числом")
        if engine_volume <= 0 or engine_volume > 10:
            raise ValueError("Объем двигателя должен быть от 0.1 до 10 литров")
        self.engine_volume: float = float(engine_volume)

    def is_off_road_vehicle(self, ground_clearance: Optional[float] = None) -> bool:
        """
        Проверяет, является ли автомобиль внедорожником.

        :param ground_clearance: Дорожный просвет в мм
        :return: True если это внедорожник, False если нет

        Примеры:
        >>> car = Car("Toyota", "Land Cruiser 200", 2018, 4.6)
        >>> car.is_off_road_vehicle()
        True
        """
        ...

    def calculate_tax(self, rate_per_liter: Union[int, float] = 75.0) -> float:
        """
        Рассчитывает транспортный налог.

        :param rate_per_liter: Ставка налога за литр объема двигателя
        :return: Сумма транспортного налога

        Примеры:
        >>> car = Car("Toyota", "Land Cruiser 200", 2018, 4.6)
        >>> car.calculate_tax()
        345.0
        """
        ...

    def get_car_features(self) -> List[str]:
        """
        Возвращает список характеристик автомобиля.

        :return: Список характеристик

        Примеры:
        >>> car = Car("Toyota", "Land Cruiser 200", 2018, 4.6)
        >>> features = car.get_car_features()
        >>> len(features)
        4
        """
        ...


class Song:
    """
    Класс для представления музыкальной композиции.
    """

    def __init__(self, title: str, artist: str, duration: int, genre: str):
        """
        Создание объекта "Песня".

        :param title: Название песни
        :param artist: Исполнитель
        :param duration: Длительность в секундах
        :param genre: Музыкальный жанр

        Примеры:
        >>> song = Song("Что я возьму с собой", "Гуф", 210, "хип-хоп")
        >>> song.title
        'Что я возьму с собой'
        >>> song.artist
        'Гуф'
        """
        if not isinstance(title, str):
            raise TypeError("Название песни должно быть строкой")
        if len(title.strip()) == 0:
            raise ValueError("Название песни не может быть пустым")
        self.title: str = title

        if not isinstance(artist, str):
            raise TypeError("Исполнитель должен быть строкой")
        if len(artist.strip()) == 0:
            raise ValueError("Исполнитель не может быть пустым")
        self.artist: str = artist

        if not isinstance(duration, int):
            raise TypeError("Длительность должна быть целым числом")
        if duration <= 0 or duration > 3600:
            raise ValueError("Длительность должна быть от 1 до 3600 секунд")
        self.duration: int = duration

        if not isinstance(genre, str):
            raise TypeError("Жанр должен быть строкой")
        if len(genre.strip()) == 0:
            raise ValueError("Жанр не может быть пустым")
        self.genre: str = genre

    def is_short_song(self, threshold: Optional[int] = None) -> bool:
        """
        Проверяет, является ли песня короткой.

        :param threshold: Пороговое значение в секундах (опционально)
        :return: True если песня короче порога, False если длиннее

        Примеры:
        >>> song = Song("Что я возьму с собой", "Гуф", 210, "хип-хоп")
        >>> song.is_short_song()
        False
        """
        ...

    def get_song_info(self) -> str:
        """
        Возвращает информацию о песне.

        :return: Строка с информацией о песне

        Примеры:
        >>> song = Song("Что я возьму с собой", "Гуф", 210, "хип-хоп")
        >>> song.get_song_info()
        'Что я возьму с собой - Гуф (03:30, хип-хоп)'
        """
        ...

    def get_related_songs(self) -> List[str]:
        """
        Возвращает список похожих песен.

        :return: Список названий похожих песен

        Примеры:
        >>> song = Song("Что я возьму с собой", "Гуф", 210, "хип-хоп")
        >>> related = song.get_related_songs()
        >>> isinstance(related, list)
        True
        """
        ...


if __name__ == "__main__":
    result = doctest.testmod(verbose=False)