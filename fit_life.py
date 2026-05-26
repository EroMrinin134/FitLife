import math, sys

# Константы.
WATER_PER_KG = 30
ML_TO_L = 0.001

MIN_BELIEVABLE_USER_WEIHGT = 3
MIN_BELIEVABLE_USER_HEIGHT = 0.5

# Функции.
def input_user_name():
    """
    Запрашивает и возвращает имя пользователя.
    Производит несколько запросов в случае некорретно введённых данных.

    Гарантии:
    - имя не будет пустой строкой
    - имя будет отформатированно
    """

    while True:
        user_name = input("Введите ваше имя: ")

        if len(user_name) == 0:
            print("Пустое имя недопустимо.")
            continue

        return user_name.title()

def input_user_age():
    """
    Запрашивает и возвращает возраст пользователя (в полных годах).
    Производит несколько запросов в случае некорретно введённых данных.

    Гарантии:
    - возраст будет неотрицательным числом (>= 0)
    """
    while True:
        user_age = input("Введите ваш возраст (в полных годах): ")

        if len(user_age) == 0:
            print("Возраст не введён.")
            continue

        try:
            user_age = int(user_age)
        except ValueError:
            print("У возраста некорретный формат числа.")
            continue

        if user_age < 0:
            print("Возраст не может быть отрицательным числом.")
            continue

        return user_age

def input_user_weight(min_believable_value = None):
    """
    Запрашивает и возвращает вес пользователя (в кг).
    Производит несколько запросов в случае некорретно введённых данных.
    При вводе запятая допустима, как разделитель.

    Гарантии:
    - вес будет обычным числом (не NaN или бесконечность)
    - вес будет положительным числом (> 0)
    """

    while True:
        user_weight = input("Введите ваш вес (в кг): ")

        if len(user_weight) == 0:
            print("Вес не введён.")
            continue

        user_weight = user_weight.replace(",", ".")

        try:
            user_weight = float(user_weight)
        except ValueError:
            print("У веса некорретный формат числа.")
            continue

        if not math.isfinite(user_weight):
            print("Вес должен быть обычным вещественным числом.")
            continue

        if user_weight <= 0:
            print("Вес должен быть положительным числом.")
            continue

        if (min_believable_value is not None
                and user_weight < min_believable_value):
            print("Вес неправдоподобно мал, пожалуйста, введите настоящий.")
            continue

        return user_weight

def input_user_height(min_believable_value = None):
    """
    Запрашивает и возвращает рост пользователя (в метрах).
    Производит несколько запросов в случае некорретно введённых данных.
    При вводе запятая допустима, как разделитель.

    Гарантии:
    - рост будет обычным числом (не NaN или бесконечность)
    - рост будет положительным числом (> 0)
    """

    while True:
        user_height = input("Введите ваш рост (в метрах): ")

        if len(user_height) == 0:
            print("Рост не введён.")
            continue

        user_height = user_height.replace(",", ".")

        try:
            user_height = float(user_height)
        except ValueError:
            print("У роста некорретный формат числа.")
            continue

        if not math.isfinite(user_weight):
            print("Рост должен быть обычным вещественным числом.")
            continue

        if user_height <= 0:
            print("Рост должен быть положительным числом.")
            continue

        if (min_believable_value is not None
                and user_height < min_believable_value):
            print("Рост неправдоподобно мал, пожалуйста, введите настоящий.")
            continue

        return user_height

# Сама программа.
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

user_name = input_user_name()
user_age = input_user_age()
user_weight = input_user_weight(MIN_BELIEVABLE_USER_WEIHGT)
user_height = input_user_height(MIN_BELIEVABLE_USER_HEIGHT)

bmi = round(user_weight / (user_height ** 2), 1)

water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml * ML_TO_L, 2)

print()
print(f"Отчёт для пользователя: {user_name} ({user_age} г.)!")
print(f"Ваш индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print("Расчёт окончен. Будьте здоровы!")
