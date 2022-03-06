class Data():
    def __init__(self, date_string):
        date_s = date_string
        Data.ext_str(date_string)

    @classmethod
    def ext_str(cls,date_string):
        date_s = {'day':int(date_string[0] + date_string[1])}
        date_s['month'] = int(date_string[3] + date_string[4])
        date_s['year'] = int(date_string[6] + date_string[7] + date_string[8] + date_string[9])
        Data.valid_method(date_s)

        return date_s

    @staticmethod
    def valid_method(date_dic):
        if (date_dic['day'] > 0 and date_dic['day'] < 32) and (date_dic['month'] > 0 and date_dic['month'] < 13) and ( date_dic['year'] > 0):
            print("Валидация прошла успешна")
        else:
            print("Вы ввели не дату")


dates = Data("01-11-2020")
dates = Data("32-11-2020")
dates = Data("31-11-2020")
dates = Data("01-13-2020")