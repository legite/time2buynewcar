from main.Str2Info import Str2Car as Car
import unittest


class CarTest(unittest.TestCase):
    # 初始化测试
    def test_init(self):
        s = 'CAR0001|2044/05/01|Volkswagen|65535|F'
        car = Car(s)
        self.assertEqual(car.id, 'CAR0001')
        self.assertEqual(car.Date, '2044/05/01')
        self.assertEqual(car.brand, 'Volkswagen')
        self.assertEqual(car.dis, 65535)
        self.assertEqual(car.fix, False)

    def test_reminder(self):
        ss = ['CAR0001|2025/04/05|Porsche|10000|F',
             'CAR0002|2029/10/14|Porsche|9000|F',
             'CAR0003|2026/08/17|Porsche|13000|F',
             'CAR0004|2027/11/01|BYD|23000|T']
        date = '2030/09/01'
        res = [1, 2, 3, 0]
        i = -1

        for s in ss:
            i += 1
            car = Car(s)
            self.assertEqual(car.reminder(date), res[i])

if __name__ == '__main__':
    unittest.main()
