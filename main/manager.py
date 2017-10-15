
# 汽车信息管理类
class manage(object):
    __slots__ = ('list', 'date', 'Info', 'Text')

    # 初始化管理对象： 汽车信息列表list，
    # 提醒时间date， 提醒信息Info， 提醒内容text
    def __init__(self, l, date):
        self.list = l
        self.date = date
        self.Info = {0:[], 1:[], 2:[], 3:[]}
        self.Text = {0:{}, 1:{}, 2:{}, 3:{}}

    # 统计汽车保养及报废信息
    def count(self):
        for car in self.list:
            n = car.reminder(self.date)
            self.Info[n].append(car)


    # 整理保养及报废信息
    def sort(self):
        for i in range(4):
            for car in self.Info[i]:
                if car.brand not in self.Text[i]:
                    self.Text[i][car.brand] = [1, car.id]
                    # self.Text[i][car.brand] = car.id
                else:
                    self.Text[i][car.brand][0] += 1
                    self.Text[i][car.brand][1] += ', ' + car.id

    # 信息展示
    def show(self):
        print('Reminder')
        print('==================')
        print()

        print('* Time-related maintenance coming soon...')
        for k in sorted(self.Text[2].keys()):
            print(k + ': ' + str(self.Text[2][k][0]) + ' (' + self.Text[2][k][1] + ')')
        print()                                                                                # 定期保养信息展示

        print('* Distance-related maintenance coming soon...')
        for k in sorted(self.Text[1].keys()):
            print(k + ': ' + str(self.Text[1][k][0]) + ' (' + self.Text[1][k][1] + ')')
        print()                                                                                # 距离保养信息展示

        print('* Write-off coming soon...')
        for k in sorted(self.Text[0].keys()):
            print(k + ': ' + str(self.Text[0][k][0]) + ' (' + self.Text[0][k][1] + ')')        # 即将报废信息展示