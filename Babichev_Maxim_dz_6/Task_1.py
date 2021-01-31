from time import sleep


class LightSignal:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Горит цвет светофора: \n '
                  f'{LightSignal.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1


LightSignal = LightSignal()
LightSignal.running()
