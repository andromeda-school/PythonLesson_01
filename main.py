import math

# Знакомство с типами данных в Python.
# а это кстати комментарии в коде

# (String - str)
# Строка - обычный текст
name = "Степан"
password = "1234"

# (Integer - int)
# Число - целое, без дробей
age = 10

# (Float - float)
# Вещественное число - с дробями и остатками
progress = 4.3

# (Boolean - bool)
# Логическое значение - True(Истина) или False(Ложь)
key = True

print("Имя : " + name)
print("Возраст: ", age, " лет")
print("Успеваемость: ", progress)

# Допустим, что за месяц успеваемость изменилась
progress = progress - 0.8
progress = progress * 1.3
print("\nУспеваемость через месяц: ", round(progress, 2))



