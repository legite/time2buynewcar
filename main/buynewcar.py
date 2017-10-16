from main.Str2Info import Str2Car as Car
from main.manager import Manage


if __name__ == '__main__':
    # 输入信息进行处理，得到汽车信息列表cars，提醒日期date
    date = input().strip().split(': ')[1]
    s = input().strip()
    cars = []
    while s != '':
        car = Car(s)
        cars.append(car)
        s = input().strip()

    # 对汽车信息进行整理，并展示保养及报废提醒信息
    M = Manage(cars, date)
    M.count()
    M.sort()
    M.show()
