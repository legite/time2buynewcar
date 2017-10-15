from main.manager import Manage
from main.Str2Info import Str2Car as Car
import unittest

ss = ['CAR0001|2025/04/05|Porsche|10000|F',
      'CAR0002|2029/10/14|Porsche|9000|F',
      'CAR0003|2026/08/17|Porsche|13000|F',
      'CAR0004|2027/11/01|BYD|23000|T']
date = '2030/09/01'

class test_manager(unittest.TestCase):
    # 初始化测试
    def test_init(self):
        cars = []
        for s in ss:
            car = Car(s)
            cars.append(car)
        m = Manage(cars, date)
        self.assertEqual(m.list, cars)
        self.assertEqual(m.date, date)

    # 功能测试
    def test_count(self):
        cars = []
        for s in ss:
            car = Car(s)
            cars.append(car)
        m = Manage(cars, date)
        m.count()
        self.assertIn(cars[0], m.Info[1])
        self.assertIn(cars[1], m.Info[2])
        self.assertIn(cars[2], m.Info[3])
        self.assertIn(cars[3], m.Info[0])

    def test_sort(self):
        cars = []
        for s in ss:
            car = Car(s)
            cars.append(car)
        m = Manage(cars, date)
        m.count()
        m.sort()
        self.assertIn(cars[0].brand, m.Text[1])
        self.assertEqual(cars[0].id, m.Text[1][cars[0].brand][1])
        self.assertEqual(m.Text[1][cars[0].brand][0], 1)

        self.assertIn(cars[1].brand, m.Text[2])
        self.assertEqual(cars[1].id, m.Text[2][cars[1].brand][1])
        self.assertEqual(m.Text[2][cars[1].brand][0], 1)

        self.assertIn(cars[2].brand, m.Text[3])
        self.assertEqual(cars[2].id, m.Text[3][cars[0].brand][1])
        self.assertEqual(m.Text[3][cars[2].brand][0], 1)

        self.assertIn(cars[3].brand, m.Text[0])
        self.assertEqual(cars[3].id, m.Text[0][cars[0].brand][1])
        self.assertEqual(m.Text[0][cars[3].brand][0], 1)


if __name__ == '__main__':
    unittest.main()