from classes import Car

def get_choice():
    while True:
        try:
            print(
                'Создать запись - 1\nВывести одну запись - 2\nВывести все записи - 3\nИзменить запись - 4\nУдалить запись - 5\nЗавершить сеанс - 6')
            choice = int(input('Что выберите?: '))
            if choice < 0:
                print('Других действий у нас нет!')
                continue
            elif choice > 6:
                print('Других действий у нас нет!')
                continue
        except ValueError:
            print('Пишите только цифры!')
            continue
        else:
            return choice


def action():
    while True:
        choice = get_choice()
        try:
            match choice:
                case 1:
                    Car.num += 0
                    print(Car.create(Car))
                    continue
                case 2:
                    idx = int(input('Какую запись показать: '))
                    print(Car.retrieve(Car, idx))
                    continue
                case 3:
                    Car.listing(Car)
                    continue
                case 4:
                    idx = int(input('Какую запись хотите изменить: '))
                    print(Car.update(Car, idx))
                    continue
                case 5:
                    idx = int(input('Какую запись хотите удалить: '))
                    print(Car.delete(Car, idx))
                    continue
                case 6:
                    print('Досвидания')
                    break
        except ValueError as e:
            print('Пишите только цифры')
            continue
        except IndexError:
            print('Такой записи нету')
            continue

def main():
    print('Здравствуйте, это база данных автомобилей')
    print('Учтите что после завершения программы ID будут сохранятся с 1 числа')
    print('С базой данных вы можете проделать следующие действия:')


    action()



