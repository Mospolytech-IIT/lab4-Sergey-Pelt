"""Функции с исключениями"""
def division_ex(a, b):
    """Функция деления, выбрасывает исключение при b == 0."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return a / b

def index_ex(lst, index):
    """Функция доступа к элементу списка, выбрасывает исключение при некорректном индексе."""
    if index >= len(lst):
        raise IndexError("Индекс за пределами списка.")
    return lst[index]

def safe_file_read(file_path):
    """Функция чтения файлас обработчиком исключения при отсутствии файла."""
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return None

def safe_division(a, b):
    """Функция деления с обработчиком исключений общего типа и блоком finally."""
    try:
        result = a / b
        return result
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    finally:
        print("Операция завершена.")

def different_ex(value):
    """Функция обработки данных, выбрасывает разные исключения при разных типах ошибок."""
    try:
        if not isinstance(value, int):
            raise TypeError("Ожидался целочисленный тип.")
        if value < 0:
            raise ValueError("Число не может быть отрицательным.")
        result = 10 / value
        return result
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except ZeroDivisionError as e:
        print(f"Ошибка деления на ноль: {e}")
    finally:
        print("Операция завершена.")

def different_ex_2(s):
    """Функция обработки строки, выбрасывает исключения при пустой строке или длинной строке."""
    try:
        if len(s) == 0:
            raise ValueError("Строка не должна быть пустой.")
        if len(s) > 10:
            raise OverflowError("Строка слишком длинная.")
        return s.upper()
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except OverflowError as e:
        print(f"Ошибка переполнения: {e}")
    finally:
        print("Обработка строки завершена.")

def different_ex_3(lst):
    """Функция деления элементов списка, выбрасывает исключения при нуле в списке."""
    try:
        return [10 / x for x in lst]
    except ZeroDivisionError as e:
        print(f"Ошибка деления на ноль в списке: {e}")
    finally:
        print("Обработка списка завершена.")

def generate_ex(value):
    """Функция, генерирующая исключения на основе входных данных."""
    try:
        if value < 0:
            raise ValueError("Число должно быть положительным.")
        elif value == 0:
            raise ZeroDivisionError("Число не должно быть равно нулю.")
        else:
            return value ** 2
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except ZeroDivisionError as e:
        print(f"Ошибка деления: {e}")
    finally:
        print("Функция завершена.")

class CustomError1(Exception):
    """Пользовательское исключение 1"""
    def __init__(self, value, message="Ошибка: значение меньше нуля"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Введённое значение: {self.value}"


class CustomError2(Exception):
    """Пользовательское исключение 2"""
    def __init__(self, value, message="Ошибка: значение равно нулю"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Введённое значение: {self.value}"


class CustomError3(Exception):
    """Пользовательское исключение 3"""
    def __init__(self, value, limit, message="Ошибка: значение больше допустимого"):
        self.value = value
        self.limit = limit  # Лимит, который был превышен
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Введённое значение: {self.value}, лимит: {self.limit}"

def check_value(value):
    """Функция выбрасывает расширенные пользовательские исключения при определённых значениях."""
    try:
        if value < 0:
            raise CustomError1(value)
        if value == 0:
            raise CustomError2(value)
        if value > 100:
            raise CustomError3(value, 100)
        return value
    except CustomError1 as e:
        print(f"Пользовательская ошибка 1: {e}")
    except CustomError2 as e:
        print(f"Пользовательская ошибка 2: {e}")
    except CustomError3 as e:
        print(f"Пользовательская ошибка 3: {e}")
    finally:
        print("Проверка значения завершена.")
