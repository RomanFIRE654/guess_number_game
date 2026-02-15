import random

liders_easy = {

}

liders_hard = {

}

avtor_name = "Roma"
name = ""
counter = 0

def game_selection ():
    print("*"*10)
    print("ВЫБЕРИТЕ РЕЖИМ ИГРЫ")
    game_select = input("1)изичный 2)хардовый...")
    if game_select =="1":
        making_game_easy(name,counter,liders_easy)
    elif game_select =="2":
        making_game_hard(name,counter,liders_hard)
    print("*"*10)

def making_game_easy(name: str,counter: int ,liders_easy: dict):
    print("*"*10)
    name = input("Введите свое имя: ")
    print(f"Добро пожаловать в режим просто игры {name}")
    random_number = random.randint(1 , 10)
    user_number = 0
    while user_number != random_number:
        print(f"Сделано попыток {counter}")
        user_number = int(input("Введите свое число(от 1 до 10)..."))
        if user_number > random_number:
            print("Искомое число меньше")
            counter = counter+1
        elif user_number < random_number:
            print("Искомое число больше")
            counter = counter+1
    else:
        counter = counter+1
        print("ПОБЕДА!!!")
        print(f"Было сделано {counter} попыток")
        liders_easy.update({name : counter})
        print(liders_easy)
        print("*"*10)
        menu_but = input("ДЛЯ ВЫХОДА В МЕНЮ НАЖМИТЕ ЛЮБУЮ КНОПКУ")

def making_game_hard(name: str,counter: int ,liders_hard: dict):
    print("*"*10)
    name = input("Введите свое имя: ")
    print(f"Добро пожаловать в режим ХАРДКОРНОЙ игры... {name}")
    random_number = random.randint(1 , 100)
    user_number = 0
    while user_number != random_number:
        print(f"Сделано попыток {counter}")
        user_number = int(input("Введите свое число(от 1 до 100 :0 ВАААУ )..."))
        if user_number > random_number:
            print("Искомое число меньше")
            counter = counter+1
        elif user_number < random_number:
            print("Искомое число больше")
            counter = counter+1
    else:
        counter = counter+1
        print("ПОБЕДА!!! ЭТО БЫЛО СЛОЖНО!!!")
        print(f"Было сделано {counter} попыток")
        liders_hard.update({name : counter})
        print(liders_hard)
        print("*"*10)
        menu_but = input("ДЛЯ ВЫХОДА В МЕНЮ НАЖМИТЕ ЛЮБУЮ КНОПКУ")

def informing(avtor_name: str):
    print("*"*10)
    print("ИНФОРМАЦИЯ ОБ АВТОРЕ:")
    print(f"Автор - {avtor_name}")
    print("*"*10)
    menu_but = input("ДЛЯ ВЫХОДА В МЕНЮ НАЖМИТЕ ЛЮБУЮ КНОПКУ")

def output_tables(liders_easy:dict,liders_hard:dict):
    print("*"*10)
    print("ВЫ ВОШЛИ В СПИСКИ ПОБЕДИТЕЛЕЙ")
    print("")
    print("Изи уровень")
    print(liders_easy)
    print("")
    print("Хард-уровень")
    print(liders_hard)
    print("*"*10)
    menu_but = input("ДЛЯ ВЫХОДА В МЕНЮ НАЖМИТЕ ЛЮБУЮ КНОПКУ")


def menu_selection(menu_select: str):
    if menu_select == "1":
        game_selection()
    elif menu_select == "2":
        output_tables(liders_easy,liders_hard)
    elif menu_select == "3":
        informing(avtor_name)
    elif menu_select == "4":
        pass
    else:
        print("Нет такого варианта....")




while True:
    print("*"*30)
    print("*"*10+"УГАДАЙ ЧИСЛО v2"+"*"*10)
    print("*"*30)
    print("")
    print("1)ИГРА")
    print("")
    print("2)СПИСКИ ЛИДЕРОВ")
    print("")
    print("3)ОБ АВТОРЕ")
    print("")
    print("4)ВЫХОД")
    print("")
    menu_select = input("Выберите...")
    if menu_select == "4":
        break
    else:
        menu_selection(menu_select)
