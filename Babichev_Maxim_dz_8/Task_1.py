class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Корректно'
                else:
                    return f'Не верно указан год'
            else:
                return f'Не верно указан месяц'
        else:
            return f'Не верно указан день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('21 - 5 - 2020')
print(today)
print(Data.valid(11, 5, 2022))
print(today.valid(11, 13, 2015))
print(Data.extract('11 - 11 - 2021'))
print(today.extract('10 - 12 - 2018'))
print(Data.valid(1, 11, 2000))
