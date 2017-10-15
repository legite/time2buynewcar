import datetime

STD = {True:[365 * 3, 3, 3], False:[365 *6, 12, 6]}                      # 寿命及定期保养标准

# 定义字符串转车辆类
class Str2Car(object):
    __slots__ = ('id', 'Date', 'brand', 'dis', 'fix')

    # 初始化车辆信息：编号id，购买日期date，品牌brand，公里数dis,是否检修fix
    def __init__(self, str):
        ss = str.split('|')
        self.id = ss[0]
        self.Date = ss[1]
        self.brand = ss[2]
        self.dis = int(ss[3])
        Fix = {'T': True, 'F':False}
        self.fix = Fix[ss[4]]

    # 保养及报废提醒
    def reminder(self, date):
        t1 = list(map(lambda x:int(x), self.Date.split('/')))
        t2 = list(map(lambda x:int(x), date.split('/')))

        d1 = datetime.date(t1[0], t1[1], t1[2])                          # 购买日期
        d2 = datetime.date(t2[0], t2[1], t2[2])                          # 检查提醒日期

        # 判断报废情况: 0-即将报废， 1-距离保养， 2-定期保养， 3-已经报废或正常
        doff = d1 + datetime.timedelta(days=STD[self.fix][0])            # 报废时间

        if ((doff.year - d2.year) * 12 + doff.month - d2.month) < 0:
            return 3                                                     # 已经报废
        elif ((doff.year - d2.year) * 12 + doff.month - d2.month) == 0:
            if (d2.day - doff.day) < 0:
                return 0                                                 # 即将报废
            else:
                return 3                                                 # 已经报废
        elif ((doff.year - d2.year) * 12 + doff.month - d2.month) == 1:
            return 0                                                     # 即将报废
        elif (self.dis % 10000) >= 9500 or (self.dis % 10000) == 0:
            return 1                                                     # 距离保养
        else:
            if (d2.year - d1.year) < 3:
                m = (d2.year - d1.year) * 12 + d2.month - d1.month
                if (m % STD[self.fix][1]) == 0:
                    if (d2.day - d1.day) <= 0:
                        return 2                                         # 定期保养
                    else:
                        return 3                                         # 正常
                elif (m + 1) % STD[self.fix][1] == 0:
                    return 2                                             # 定期保养
                else:
                    return 3                                             # 正常
            else:
                m = (d2.year - d1.year) * 12 + d2.month - d1.month
                if (m % STD[self.fix][2]) == 0:
                    if (d2.day - d1.day) <= 0:
                        return 2                                         # 定期保养
                    else:
                        return 3                                         # 正常
                elif (m + 1) % STD[self.fix][2] == 0:
                    return 2                                             # 定期保养
                else:
                    return 3                                             # 正常