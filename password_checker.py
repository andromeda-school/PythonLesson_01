#
#   Программа по проверке пароля.
#    Eсли пароль верный, программа дает возможность
#    обновить прогресс пользователя по его желанию.
#
#   Здесь нам нужно использовать конструкцию
#       if (условие):
#           ...
#       else:
#           ...
#

name = "Степан"
age = 10
progress = 4.3
password = "1234"
inputValue = input("Введите пароль: ")

if(inputValue == password):
    print("Успешно!")
    print("Добро пожаловать,", name)
    print("Ваш прогресс:", progress)
    inputValue = input("Добавить прогресс? ")
    if(inputValue == "да"):
        inputValue = float(input("Введите на сколько: "))
        progress = progress + inputValue
        print("Успешно!")
        print("Ваш новый прогресс:", progress)
    else:
        print("Хорошего дня!")
else:
    print("Пароль не верный.")
