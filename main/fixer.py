from main.Str2Info import  Str2Car as Car
from main.manager import manage

if __name__ == '__main__':

    date = input().split(': ')[1]
    s = input()
    cars = []
    while s != '':
        car = Car(s)
        cars.append(car)
        s = input()

    M = manage(cars, date)
    M.count()
    M.sort()
    M.show()