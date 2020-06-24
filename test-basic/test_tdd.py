# -- coding: utf-8 --
import unittest


#สร้าง ฟังชั่น ทีหลัง         [1]
def add_num(a, b):
    return a + b

# เขียน unittest ก่อน
class MyTest(unittest.TestCase):

    def test_add_first(self):           #เขียนเพื่อให้ผ่าน           [2]
        self.assertEqual(3,3)

    def test_add(self):             #refactor code              [3]
        result = add_num(1, 2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
