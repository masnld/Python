if __name__ == "__main__":
    class Car:
        """Базовый класс "Автомобиль"."""

        def __init__(self, brand: str, model: str, year: int) -> None:
            """
            Конструктор базового класса.

            Args:
                brand (str): марка автомобиля
                model (str): модель автомобиля
                year (int): год выпуска
            """
            self._brand = brand
            self.model = model
            self.year = year

        def __str__(self) -> str:
            """Возвращает строковое представление автомобиля."""
            return f"{self._brand} {self.model}, {self.year} год"

        def __repr__(self) -> str:
            """Возвращает официальное строковое представление."""
            return f"{self.__class__.__name__}(brand={self._brand!r}, model={self.model!r}, year={self.year!r})"

        def vehicle_info(self) -> str:
            """Метод для получения общей информации о транспортном средстве."""
            return f"{self._brand} {self.model}, {self.year} год выпуска"


    class PassengerCar(Car):
        """Дочерний класс 'Легковой автомобиль'."""

        def __init__(self, brand: str, model: str, year: int, engine: float) -> None:
            """
            Конструктор дочернего класса.
            Расширяет конструктор базового класса новым атрибутом.

            Args:
                brand (str): марка автомобиля
                model (str): модель автомобиля
                year (int): год выпуска
                engine (float): объём двигателя в литрах
            """
            super().__init__(brand, model, year)
            self.engine = engine

        def __str__(self) -> str:
            """
            Переопределение метода __str__.
            Причина: требуется включить информацию о двигателе.
            """
            return f"{self._brand} {self.model}, {self.year} год, {self.engine} л. двигатель"

        def __repr__(self) -> str:
            """Переопределение __repr__ с учётом нового атрибута engine."""
            return f"{self.__class__.__name__}(brand={self._brand!r}, model={self.model!r}, year={self.year!r}, engine={self.engine!r})"

        def car_info(self) -> str:
            """
            Переопределение метода vehicle_info.
            Причина: для легкового автомобиля важно показывать объём двигателя,
            поэтому добавляем эту информацию к базовой версии.
            """
            base_info = super().vehicle_info()
            return f"{base_info}, двигатель: {self.engine} л."

    if __name__ == "__main__":
        passenger_car = PassengerCar("Toyota", "Land Cruiser 200", 2018, 4.6)
        print(passenger_car)
        print(repr(passenger_car))
        print(passenger_car.car_info())

pass
