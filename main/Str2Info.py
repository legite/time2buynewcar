
#定义字符串转换类
class Str2Car(object):

    def __init__(self, str):
        ss = str.split('|')
        self.id = ss[0]
        self.date = ss[1]
        self.branch = ss[2]
        self.distance = int(ss[3])
        Fix = {'T': True, 'F':False}
        self.fix = Fix[ss[4]]
