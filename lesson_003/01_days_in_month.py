# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом


month_day_count = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31,
    '45':100
}

user_input = input("Введите, пожалуйста, номер месяца: ") #просим пользователя ввеси номер месяца
if user_input.isdigit(): # говорим питону что введеное пользователем число тлоько номер(не текст)
    month = int(user_input)

    if 1 <= month <= 12: # Говорим что если месяц от 1 до 12
        day_count = month_day_count[user_input] # приравниваем количество дней к количуству дней в месяце из словаря
        print('Вы ввели', month)
        print('Кол-во дней в месяце:', day_count)
    else: # говорим о том что если не соблюдается услови от 1 до 12 то выводим текст
        print('Месяца с таким номером не существует!')
else: # если человек вводит буквы вместо чисел выводим текст
    print('Only number of month!')
