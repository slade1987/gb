class Warehouse():
    '''
    Класс склад.
    Можно помещаться вещать, просматривать и забирать вещи со склада.
    '''
    __size_of_warehouse = 0
    __used_size = 0
    __list_of_device = []
# Сделать проверки на вводимые данные которые написаны в задании
    def __init__(self,size: int):
        if str(size).isdigit():
            self.__size_of_warehouse = size
        else:
            print("Вы ввели некоректные данные")

    # def передать технику на склад
    def put_on_warehouse(self,device):
        if str(device).isdigit():
            if self.__used_size > self.__size_of_warehouse:
                print("Склад заполнен. Освободите или расширьте склад")
            else:
                self.__list_of_device.append(device)
                self.__used_size += 1
        else:
            print("Вы ввели некоректные данные")

    # def показать все устройства на складе
    def show_warehouse(self):
        if self.__used_size > 0:
            num = 0
            for i in self.__list_of_device:
                num += 1
                print(num," ) ",i)
        else:
            print("Склад пуст.")

    # def забрать устрофство со склада с проверкой забираемого итема.
    def pop_device(self,i: int):
        if str(i).isdigit():
            if (i - 1) < self.__used_size:
                self.__list_of_device.pop(i - 1)
            else:
                print("Номера с такой позицией нет")
        else:
            print("Вы ввели некоректные данные")

    #def расширение склада
    def resize_warehouse(self, s: int):
        if str(s).isdigit():
            self.__size_of_warehouse = s
        else:
            print("Вы ввели некоректные данные")


#!!!!!!!!!! Удалить коменты
# Скорее всего нужно разделить классы Готовые классы

class Equipment():
    '''
    Класс оборудование виртуальный класс
    '''
    def __init__(self,s,r,n,m):
        self.speed = s
        self.resource = r
        self.name = n
        self.model = m

    def return_info(self):
        return self.name + ' ' + self.model


#По заданию нужно разделеить класс на несльколько ((((((((((((((((((((((
class Printer(Equipment):

    '''
    Класс принтер
    '''

    def __init__(self,s,r,n,m,type_printer):
        super().__init__(s,r,n,m)
        self.type_printer = type_printer


class Copier(Equipment):

    '''
     Класс копир
    '''

    def __init__(self,s,r,n,m,max_papaer_format):
        super().__init__(s, r, n, m)
        self.paper = max_papaer_format

class MFU(Equipment):

    '''
     Класс МФУ
    '''

    def __init__(self, s, r, n, m, connection_type):
        super().__init__(s, r, n, m)
        self.connection = connection_type


new_warehouse = Warehouse(1)

printer = Printer(100,1000,"Kyocera","2055","Лазерный")
copir = MFU(50,1000,"HP","3209dn","USB RJ45")
xerox = Copier(10,10000,"Canon","FC128","A3")


new_warehouse.put_on_warehouse(xerox.return_info())
new_warehouse.put_on_warehouse(copir.return_info())
# Ошибка переполнения склада
new_warehouse.put_on_warehouse(printer.return_info())
# Вывод информации о находящейся техники на складеы
new_warehouse.show_warehouse()
print('----------------')
#Расширение склада.
new_warehouse.resize_warehouse(5)
new_warehouse.put_on_warehouse(printer.return_info())
# Вывод информации о находящейся техники на складеы
new_warehouse.show_warehouse()
print('----------------')
new_warehouse.pop_device(2)
new_warehouse.show_warehouse()
# Ошибка удаления не существующео объекта
new_warehouse.pop_device(22)
print('----------------')
new_warehouse.resize_warehouse("fdsfasdf")

