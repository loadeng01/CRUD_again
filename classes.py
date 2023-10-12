import json

class WriteToJsonMixin:
    def write_to_json(self, elements):
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(elements, file, ensure_ascii=False, indent=4)


class ReadJsonMixin:
    def read_json(self):

        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                if not data:
                    print("JSON файл пустой.")
                else:
                    pass
        except json.JSONDecodeError:
            print("База данных пуста")
            return []
        except FileNotFoundError:
            print("Файл не найден.")
            return []
        else:
            return data

class WriteMixin:
    def write(self):
        element = {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'engine_value': float(self.engine_val),
            'color': self.color,
            'body_type': self.body_type,
            'mileage': self.mileage,
            'price': float(self.price)
        }



        elements = self.read_json()

        elements.append(element)

        self.write_to_json(elements)


class CreateMixin:
    def create(self):
        brand = input('Марка машины: ')
        model = input('Модель: ')
        year = int(input('Год выпуска: '))
        engine_val = float(input('Обьем двигателя: '))
        color = input('Цвет: ')
        body_type = input('Кузов: ')
        mileage = input('Пробег: ')
        price = float(input('Цена: '))
        Car(brand, model, year, engine_val, color, body_type, mileage, price)

        return 'Запись успешно создана'

class ListingMixin:
    def listing(self):
        elements = self.read_json(self)

        for element in elements:
            print(element)


class RetrieveMixin:
    def retrieve(self, idx):
        elements = self.read_json(self)

        car = list(filter(lambda element: element['id'] == idx, elements))[0]

        return car

class UpdateMixin:
    def update(self, idx):
        elements = self.read_json(self)


        while True:
            try:

                car = list(filter(lambda element: element['id'] == idx, elements))[0]
                idx = elements.index(car)
                elements[idx]['brand'] = input('Марка машины: ')
                elements[idx]['model'] = input('Модель: ')
                elements[idx]['year'] = int(input('Год выпуска: '))
                elements[idx]['engine_val'] = float(input('Обьем двигателя: '))
                elements[idx]['color'] = input('Цвет: ')
                elements[idx]['body_type'] = input('Кузов: ')
                elements[idx]['mileage'] = input('Пробег: ')
                elements[idx]['price'] = float(input('Цена: '))

            except ValueError:
                print('Ошибка ввода')
                continue
            else:
                self.write_to_json(self, elements)
                return 'Запись успешно изменена'


class DeleteMixin:
    def delete(self, idx):
        elements = self.read_json(self)

        car = list(filter(lambda element: element['id'] == idx, elements))[0]
        elements.remove(car)

        self.write_to_json(self, elements)
        return 'Запись успешно удалена'


class Car(WriteMixin, ReadJsonMixin, WriteToJsonMixin, CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    num = 1

    def __init__(self, brand, model, year, engine_val, color, body_type, mileage, price):
        from decimal import Decimal
        self.id = Car.num
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_val = Decimal(engine_val).quantize((Decimal('1.0')))
        self.color = color
        self.body_type = body_type
        self.mileage = mileage
        self.price = Decimal(str(price)).quantize((Decimal('1.00')))
        Car.num += 1
        self.write()