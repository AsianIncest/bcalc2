def say_hello():
    print("""Привет! Есть 2 режима работы:
    1) Введи один коэффициент для того чтобы расчитать противоположную сторону.
    2) Введи 2 или более чтобы посчитать вероятности и маржу.""")

import math
class Bet:
    def __init__(self):
        self.raw_kef = ""
        self.mode = 0
        self.one_kef = 1
        self.multi_kef = []
        self.accuracy_percent = 2
        self.accuracy_kef = 1
        self.other_kef = 0
        self.rounded_other_kef = 1
        self.rounded_percent = 0
        self.rounded_marja = 0

    def prompt(self, txt="-> "):
        self.raw_kef = input(txt)
        self.mode = 2 if " " in self.raw_kef else 1
        if self.mode == 1:
            try:
                self.one_kef = float(self.raw_kef)
            except:
                print("Режим 1, ошибка ввода!")
        elif self.mode == 2:
            try:
                self.multi_kef = [float(i) for i in self.raw_kef.split(" ")]
            except:
                print("Режим 2, ошибка ввода!")
                return [0]
        self.calculate()

    def calculate(self):
        if self.mode == 1:
            if self.one_kef == 0:
                self.one_kef = 1
                print("Ошибка! Нулевой кеф!")
            p = 1 / self.one_kef * 100
            self.other_kef = 1.0 if self.one_kef == 1 else 1 / (100 - p) * 100
            self.rounded_other_kef = round(self.other_kef, self.accuracy_kef)
        elif self.mode == 2:
            try:
                self.percent = [math.pow(i, -1) * 100 for i in self.multi_kef]
                self.sum_percent = sum(self.percent)
                self.marja = self.sum_percent - 100 if self.sum_percent > 100 else 0
                self.rounded_percent = [str(round(i - self.marja, self.accuracy_percent))+"%" for i in self.percent]
                self.rounded_marja = str(round(self.marja, self.accuracy_percent))+"%"
            except:
                print("Ошибка! Неправильный кеф!")
        else:
            print("Неверный режим")


say_hello()
b = Bet()
while 1:
    b.prompt()
    if b.mode == 1:
        print(b.one_kef, "<-->", b.rounded_other_kef)
    else:
        print("-> ", b.rounded_percent, f"@ {b.rounded_marja}")
