import random


def gaming1(name:str, liders):
    print("ЛЕГКИЙ РЕЖИМ ИГРЫ(от 1 до 10)")
    a = random.randint(1, 10)
    b = 0
    i = 1
    while b != a:
        b = int(input(f"Угадай число от 1 до 10 попытка - {i} попытка...."))
        if b > a:
            print("Искомое меньше...")
            i = i+1
        elif b < a:
            print("Искомое больше...")
            i = i+1
    else:
        print(f"ПОБЕДА всего {i} попыток")
        print(f"{name}, ты искал число {a} - {i} попыток")
        liders[name] = i
        print("Таблица Лидеров :")
        print(liders)




def gaming2(name:str, liders):
    print("СЛОЖНЫЙ РЕЖИМ ИГРЫ(от 1 до 100)")
    a = random.randint(1, 100)
    b = 0
    i = 1
    while b != a:
        b = int(input(f"Угадай число от 1 до 100 попытка - {i} попытка...."))
        if b > a:
            print("Искомое меньше...")
            i = i+1
        elif b < a:
            print("Искомое больше...")
            i = i+1
    else:
        print(f"ПОБЕДА всего {i} попыток")
        print(f"{name}, ты искал число {a} - {i} попыток")
        liders[name] = i
        print("Таблица Лидеров :")
        print(liders)

def speak (avtor_name: str):
    a =(f"{avtor_name} автор программы")
    return a

def levaling(leval : str, name:str,liders):
    if leval == "1":
        gaming1(name,liders)
    elif leval == "2":
        gaming2(name,liders)
    else:
        print("Нет такого варианта")




def menu (levaling, gaming1, gaming2, speak):
    avtor_name = "Рома"
    liders = {

    }


    print("/"*30)
    print("/"*9 +"УГАДАЙ ЧИСЛО" + "/"*8)
    print("/"*30)
    print("МЕНЮ:")
    print(" 1)ИГРА")
    print(" 2)Таблица лидеров")
    print(" 3)Об Авторе")
    print(" 4)[Выход]")
    input_menu = input("выберите вариант...")

    if input_menu == "1":
        print("Вы выбрали ИГРУ...")
        name = input("Введите свое имя...")
        liders.update({name: 0})
        print(liders)
        print("1)легкий уровень 2) сложный уровень")
        leval = input("Какой выберишь?")
        levaling(leval, name, liders)

    elif input_menu == "2":
        print("Вы выбрали таблицу ЛИДЕРОВ...")
        print(liders)
    elif input_menu == "3":
        print("Вы выбрали ИНФУ ОБ АВТОРЕ...")
        speak(avtor_name)
    elif input_menu == "4":
        print("Пока")



print(menu(levaling, gaming1, gaming2, speak))
