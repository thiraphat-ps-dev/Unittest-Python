# -- coding: utf-8 --
import unittest


def add(x, y):
    return x + y


def multipy(x, y):
    return x * y


def divi(x, y):
    return x / y


def minus(x, y):
    return x - y


class TestCase(unittest.TestCase):

    def test_add(self):
        result = add(4, 6)
        act = 10
        self.assertEqual(
            result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))

    def test_multiply(self):
        result = multipy(4, 2)
        act = 8
        self.assertEqual(
            result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))

    def test_divi(self):
        result = divi(4, 2)
        act = 2
        self.assertEqual(
            result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))

    def test_minus(self):
        result = minus(14, 2)
        act = 12
        self.assertEqual(
            result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))


if __name__ == '__main__':
    unittest.main()
