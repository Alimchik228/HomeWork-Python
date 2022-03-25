from abc import ABC, abstractmethod


class equipment:
    id_equipment = 0

    def __init__(self, name_equipment):
        self.name_equipment = name_equipment
        self.id_equipment = equipment.id_equipment
        equipment.id_equipment += 1

    def action(self):
        pass


class printer(equipment):

    def action(self, stroka):
        print(stroka)
        return 0


class skan(equipment):

    def action(self, copy):
        return copy


class kser(equipment):

    def action(self, copy):
        print('выберете количество копий')
        n = int(input())
        return copy * n


class office:

    def __init__(self):
        self.equipments = {}

    def take_equipment(self, equipments):
        for key, value in equipments.items():
            if key in self.equipments:
                self.equipments[key] += value
            else:
                self.equipments[key] = value

    def give_equipment_to_union(self, union, equipment):
        if equipment.id_equipment in self.equipments and self.equipments[equipment.id_equipment] > 0:
            if union.take_equipment(equipment):
                self.equipments[equipment.id_equipment] -= 1

    def __str__(self):
        print(f'Название организации: {self.title}')
        for i in range(len(self.list)):
            print(f'Техника организации: {self.list[i].name_equipment}')
        return ''

class union:

    def __init__(self, title):
        self.title = title
        self.list = []



    def take_equipment(self, equipment):
        if len(self.list) < 3:
            self.list.append(equipment)
            return True
        else:
            print('Превышен лимит техники!')
            return False

    def give_equipment(self, equipment):
        if equipment in self.list:
            self.list.remove(equipment)
            return True
        return False
    def __str__(self):
        print(f'Название организации: {self.title}')
        for i in range (len(self.list)):
            print(f'Техника организации: {self.list[i].name_equipment}')
        return ''

class MyException(Exception):

    def __init__(self, value):
        self.value = value
# Создаем технику
printer_1 = printer('Принтер')
skan_1 = skan('Ленова')
kser_1 = kser('Самсунг')
equipments = {printer_1.id_equipment: 5,
              skan_1.id_equipment: 6,
              kser_1.id_equipment: 2}

if type(equipments.get(printer_1.id_equipment)) != int:
    raise MyException('Вводите только цифры!')
# print(printer_1.id_equipment)
# print(skan_1.id_equipment)
# print(kser_1.id_equipment)
# Создаем и добавляем склад
office_1 = office()
office_1.take_equipment(equipments)
print(office_1.equipments)
# Создаем раздел
union_1 = union('DNS')
print(union_1.title)
print(union_1.list)
office_1.give_equipment_to_union(union_1, printer_1)
office_1.give_equipment_to_union(union_1, printer_1)
print(union_1)
print(office_1.equipments)
