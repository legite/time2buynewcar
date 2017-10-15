
class show(object):
    def __init__(self, l1, l2, l3):
        self.off = {}
        self.dis = {}
        self.time = {}

        for l in l1:
            if l.branch not in self.off:
                self.off[l.branch] = [1, l.id]
            else:
                self.off[l.branch][0] += 1
                self.off[l.branch][1] = self.off[l.branch] + ', ' + l.id
        for l in l2:
            if l.branch not in self.dis:
                self.dis[l.branch] = [1,l.id]
            else:
                self.dis[l.branch][0] += 1
                self.dis[l.branch][1] = self.dis[l.branch] + ', ' + l.id
        for l in l3:
            if l.branch not in self.time:
                self.time[l.branch] = [1, l.id]
            else:
                self.time[l.branch][0] += 1
                self.time[l.branch][1] = self.time[l.branch] + ', ' + l.id

    def print(self):
        print('Reminder')
        print('==================')

        print('* Time-related maintenance coming soon...')
        for k in sorted(self.time.keys()):
            print(k + ': ' + str(self.time[k][0]) + ' (' + self.time[k][1] + ')')
        print()

        print('* Distance-related maintenance coming soon...')
        for k in sorted(self.dis.keys()):
            print(k + ': ' + str(self.dis[k][0]) + ' (' + self.dis[k][1] + ')')
        print()

        print('* Write-off coming soon...')
        for k in sorted(self.off.keys()):
            print(k + ': ' + str(self.off[k][0]) + ' (' + self.off[k][1] + ')')
