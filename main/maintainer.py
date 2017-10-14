
# 保养以及报废状况类
class maintain(object):
    def __init__(self, car, date):
        self.car = car
        self.date = date

    def reminder(self):
        # 行驶距离保养标准，以及标记
        if self.car.distance == 10000:
            return 0
        elif (self.car.distance % 10000) > (10000 - 500):
            return 0

        # 定期保养，以及标记
        if self.car.fix:



def datenum(str1, str2):
    return [0, 0, 0]