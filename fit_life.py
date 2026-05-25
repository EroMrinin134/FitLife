# Проект FitLife - MVP версия 1.0

import sys

# Явно устанавливаем кодировку, чтобы тесты отрабатывали.
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# 1. Знакомство
while True:
    user_name = input("Введите ваше имя: ")

    if len(user_name) == 0:
        print("Пустое имя недопустимо.")
        continue

    # Конец валидации.
    break

while True:
    user_age = input("Введите ваше возраст: ")

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

    # Конец валидации.
    break

# 2. Сбор данных
while True:
    user_weight = input("Введите ваш вес (в кг): ")

    if len(user_weight) == 0:
        print("Вес не введён.")
        continue

    # Запятая допустима, как разделитель.
    user_weight = user_weight.replace(",", ".")

    try:
        user_weight = float(user_weight)
    except ValueError:
        print("У веса некорретный формат числа.")
        continue

    if user_weight < 0:
        print("Вес не может быть отрицательным числом.")
        continue

    # Конец валидации.
    break

while True:

    user_height = input("Введите ваш рост (в метрах): ")

    if len(user_height) == 0:
        print("Рост не введён. Пожалуйста, попробуйте снова.")
        continue

    # Запятая допустима, как разделитель.
    user_height = user_height.replace(",", ".")

    try:
        user_height = float(user_height)
    except ValueError:
        print("У роста некорретный формат числа.")
        continue

    if user_height < 0:
        print("Рост не может быть отрицательным числом.")
        continue

    # Конец валидации.
    break

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Подсчет воды: вес * 30 мл
WATER_PER_KG = 30
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / 1000

# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)!")
print(f"Ваш индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print("Расчет окончен. Будьте здоровы!")
